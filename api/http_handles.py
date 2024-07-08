from typing import Annotated
from fastapi import FastAPI, Form

from constants.constants import Constants, ResponseCodes
from constants.urls import ToFrontendUrls
from config.env_paras import EnvParas
from actions.interact_with_bot import BotInteracter
from models.http_responses import *

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
