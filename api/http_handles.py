from typing import Annotated, Optional
from fastapi import Body, FastAPI, Form
from pydantic import BaseModel
from constants.constants import Constants, ResponseCodes
from constants.urls import ToFrontendUrls, ToTeleUrls
from config.env_paras import EnvParas
from actions.interact_with_bot import BotInteracter
from models.http_responses import *
from utils.log_util import logger

app = FastAPI()

# Check if the message field is present in the Update object if update.message: message_text = update.message.get('text', 'No text provided') print(f"Received message: {message_text}") # Process the message as needed return {"status": "success", "message": message_text} else: raise HTTPException(status_code=400, detail="No message in Update object")
class Update(BaseModel):
    message: Optional[dict] = None

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


@app.post(ToTeleUrls.REC_MESSAGE_V1)
def rec_message_v1(update: Update):
    print("rec data:", update)
