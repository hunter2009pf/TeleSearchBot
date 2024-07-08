import requests
from http import HTTPStatus

from constants.urls import Urls
from utils.log_util import logger


class BotInteracter:
    def __init__(self, bot_token: str):
        self.bot_token = bot_token

    def send_message(self, chat_id, text) -> bool:
        """
        Send a message to a Telegram group using a bot.

        :param bot_token: The token of your Telegram bot.
        :param chat_id: The unique identifier for the target chat or username of the target channel.
        :param text: The text of the message to be sent.
        """
        url = Urls.get_send_message_url(self.bot_token)

        data = {"chat_id": chat_id, "text": text}

        response = requests.post(url, json=data)

        # 检查请求是否成功
        if response.status_code == HTTPStatus.OK:
            response_data = response.json()
            if response_data["ok"]:
                logger.info("Message sent successfully!")
                return True
            else:
                logger.error(f"Error: {response_data['description']}")
                return False
        else:
            logger.error(f"Request failed with status code {response.status_code}")
            return False
