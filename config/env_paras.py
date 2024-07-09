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
        cls.DOMAIN = os.getenv("DOMAIN")  # 网关服务域名,外网访问地址
        cls.ELASTIC_HOST = os.getenv("ELASTIC_HOST")  # ES主机
        cls.ELASTIC_USER = os.getenv("ELASTIC_USER")  # ES用户名
        cls.ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD")  # ES密码

        # CHAT_ID = os.getenv("GROUP_ID")  # 群组ID
        # GROUP_LINK = os.getenv("GROUP_LINK")
        # MESSAGE_TEXT = f"邀请您加入群聊：{GROUP_LINK}"
