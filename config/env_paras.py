import os
from dotenv import load_dotenv

from constants.constants import Constants


class EnvParas:
    @classmethod
    def get_env(cls):
        load_dotenv(
            Constants.ENVIRONMENT_FILE_NAME
        )  # take environment variables from config.env.
        # read environment variables to memory
        cls.ROBOT_TOKEN = os.getenv("ROBOT_TOKEN")  # 替换为你的bot token
        cls.CHAT_ID = os.getenv("USER_ID")  # 用户ID
        # CHAT_ID = os.getenv("GROUP_ID")  # 群组ID
        # GROUP_LINK = os.getenv("GROUP_LINK")
        # MESSAGE_TEXT = f"邀请您加入群聊：{GROUP_LINK}"
