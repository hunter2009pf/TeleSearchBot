import requests
import os

from http import HTTPStatus
from dotenv import load_dotenv


def init_config():
    load_dotenv("config.env")  # take environment variables from config.env.


def send_message(bot_token, chat_id, text):
    """
    Send a message to a Telegram group using a bot.
    
    :param bot_token: The token of your Telegram bot.
    :param chat_id: The unique identifier for the target chat or username of the target channel.
    :param text: The text of the message to be sent.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    data = {
        "chat_id": chat_id,
        "text": text
    }
    
    response = requests.post(url, json=data)
    
    # 检查请求是否成功
    if response.status_code == HTTPStatus.OK:
        response_data = response.json()
        if response_data['ok']:
            print("Message sent successfully!")
        else:
            print(f"Error: {response_data['description']}")
    else:
        print(f"Request failed with status code {response.status_code}")

if __name__=="__main__":
    init_config()
    # 使用示例
    ROBOT_TOKEN = os.getenv("ROBOT_TOKEN")  # 替换为你的bot token
    CHAT_ID = os.getenv("GROUP_ID")  # 群组ID
    MESSAGE_TEXT = '晚上好，这是一条来自于中国区块链的机器人通知消息！'
    send_message(ROBOT_TOKEN, CHAT_ID, MESSAGE_TEXT)