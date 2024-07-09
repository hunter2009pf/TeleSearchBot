import argparse
import asyncio
import time
import requests
from asyncio import Queue
from http import HTTPStatus
import uvicorn
import threading
from telegram import Bot
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

from api.http_handles import app
from config.env_paras import EnvParas
from constants.constants import Constants
from constants.urls import Urls
from utils.log_util import logger


async def run_set_webhook():
    print("start set webhook")
    bot_agent = Bot(token=EnvParas.ROBOT_TOKEN)

    value = await bot_agent.set_webhook(
        url=f"{EnvParas.DOMAIN}/v1/robot/receiveMessage"
    )
    print("flesh set webhook value:", value)


def run_async_in_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(run_set_webhook())
    try:
        loop.run_until_complete(task)
    finally:
        loop.close()


def start_service():
    print("start service...")

    thread = threading.Thread(target=run_async_in_thread)
    thread.daemon = True  # 设置为守护线程，以便在主程序退出时自动结束
    thread.start()

    parser = argparse.ArgumentParser(description="Your application description.")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address")
    parser.add_argument("--port", type=int, default=8888, help="Port number")
    args = parser.parse_args()
    uvicorn.run(app=app, host=args.host, port=args.port, log_level="info")


# 定义命令和消息处理函数
def start_command(update: Update, context: CallbackContext):
    update.message.reply_text("Hi!")


def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Echo: " + update.message.text)


def __query_messages():
    # 你的 Telegram Bot Token
    API_TOKEN = EnvParas.ROBOT_TOKEN

    # 构造 getUpdates 方法的 URL
    url = Urls.get_get_updates_url(API_TOKEN)
    offset = Constants.DEFAULT_OFFSET
    while True:
        # 每隔 10 秒查询一次消息
        time.sleep(Constants.DEFAULT_ROUND_QUERY_TIEM_INTERVAL_IN_SECONDS)
        logger.info("Start to query messages")
        # 发送 GET 请求
        if offset == Constants.DEFAULT_OFFSET:
            response = requests.get(url)
        else:
            response = requests.get(url, params={"offset": offset})

        # 检查请求是否成功
        if response.status_code == HTTPStatus.OK:
            # 解析 JSON 响应
            updates = response.json()
            # 打印更新信息
            logger.info(updates)
            # 检查是否有更新
            if "result" in updates:
                for update in updates["result"]:
                    # 打印每条更新的详细信息
                    logger.info(f"Update ID: {update['update_id']}")
                    temp_update_id = update["update_id"] + 1
                    if temp_update_id > offset:
                        offset = temp_update_id
                    # 如果更新包含消息
                    if "message" in update:
                        logger.info(f"Message: {update['message']['text']}")
        else:
            logger.info(f"Failed to get updates, status code: {response.status_code}")


def __start_thread():
    # 创建并启动子线程
    thread = threading.Thread(target=__query_messages)
    thread.daemon = True  # 设置为守护线程，以便在主程序退出时自动结束
    thread.start()
