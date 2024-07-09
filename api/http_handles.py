from typing import Annotated
from fastapi import Body, FastAPI, Form

from api.task_handles import TaskFactory
from constants.constants import Constants, ResponseCodes
from constants.urls import ToFrontendUrls, ToTeleUrls
from config.env_paras import EnvParas
from actions.interact_with_bot import BotInteracter
from models.http_responses import *
from models.http_requests import *
from models.tele_message import Message
from utils.log_util import logger

app = FastAPI()


@app.get(ToFrontendUrls.VERSION_URL)
def get_version():
    return VersionResponse(
        service_name=Constants.SERVICE_NAME, version=Constants.VERSION
    )


@app.post(ToFrontendUrls.SEND_MESSAGE_URL_V1)
def send_message_v1(chat_id: Annotated[str, Form()], text: Annotated[str, Form()]):
    bi = BotInteracter(EnvParas.ROBOT_TOKEN)
    is_ok = bi.send_message(chat_id, text)
    if is_ok:
        return SimpleResponse(
            code=ResponseCodes.OK, message="Message sent successfully"
        )
    else:
        return SimpleResponse(
            code=ResponseCodes.ERROR, message="Failed to send message"
        )


@app.post(ToTeleUrls.RECEIVE_MESSAGE_V1)
def receive_message_v1(update: Update):
    logger.info(f"receive data: {update}")
    if update.message is None:
        logger.error("No message in update")
    else:
        msg: Message = update.message
        logger.info(f"text: {msg['text']}")
        message: Message = Message.from_dict(msg)
        h = TaskFactory().get_handle(message)
        h.handle(message)
