from abc import ABC
from models.tele_message import Message
from classifiers.message_classifier import MessageClassifier
from constants.constants import TaskTypes
from actions.interact_with_bot import BotInteracter
from config.env_paras import EnvParas
from utils.log_util import logger


class TaskFactory:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(TaskFactory, cls).__new__(cls)
        return cls.instance

    def get_handle(self, message: Message):
        text = message.text
        task_type = MessageClassifier.classify(text)
        match task_type:
            case TaskTypes.ASK_CHATGPT:
                return ChatGptHandle()
            case TaskTypes.SEARCH_KEYWORD:
                return SearchKeywordHandle()
            case TaskTypes.DO_NOTHING:
                return DefaultHandle()


class BaseHandle(ABC):
    def handle(self, message: Message):
        pass


class DefaultHandle(BaseHandle):
    def handle(self, message: Message):
        pass


class ChatGptHandle(BaseHandle):
    def handle(self, message: Message):
        # echo message back
        bi = BotInteracter(EnvParas.ROBOT_TOKEN)
        result = bi.send_message(message.from_data.id, message.text)
        if result:
            logger.info(f"Echo message back to {message.from_data.id} successfully")
        else:
            logger.error(f"Failed to echo message back to {message.from_data.id}")


class SearchKeywordHandle(BaseHandle):
    def handle(self, message: Message):
        # recommend Ton channel and Ton group
        bi = BotInteracter(EnvParas.ROBOT_TOKEN)
        # 假设你已经有了群组和频道的邀请链接
        group_link = "https://t.me/tondev_eng"
        channel_link = "https://t.me/toncontests"
        # 创建文本，包含群组和频道的链接
        recommendation = (
            "为您检索到以下群组和频道：\n"
            f"Ton开发者群组：{group_link}\n"
            f"Ton竞赛频道：{channel_link}"
        )
        result = bi.send_message(message.from_data.id, recommendation)
        if result:
            logger.info(f"Echo message back to {message.from_data.id} successfully")
        else:
            logger.error(
                f"Failed to send recommendation back to {message.from_data.id}"
            )
