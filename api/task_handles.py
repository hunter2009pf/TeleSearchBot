from abc import ABC

from builders.searchbuilders.base_search_builder import BaseSearchBuilder
from models.tele_message import Message
from classifiers.message_classifier import MessageClassifier
from constants.constants import TaskTypes, ElasticIndices
from actions.interact_with_bot import BotInteracter
from config.env_paras import EnvParas
from services.elastic_service import ElasticService
from utils.log_util import logger
from common.llm_manager import LLMManager


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
        # ask Kimi about the question
        # first of all, check if the kimi client exists
        # if not, create one
        session_id = message.from_data.id
        if session_id in LLMManager.kimi_client_map:
            client = LLMManager.kimi_client_map[session_id]
        else:
            client = LLMManager.create_kimi_client(session_id)
        # then, send the question to kimi
        answer = client.generate_response(message.text)
        # finally, get the answer from kimi and send it back to the user
        bi = BotInteracter(EnvParas.ROBOT_TOKEN)
        result = bi.send_message(message.from_data.id, answer)
        if result:
            logger.info(f"send answer back to {message.from_data.id} successfully")
        else:
            logger.error(f"Failed to send answer back to {message.from_data.id}")


class SearchKeywordHandle(BaseHandle):
    def handle(self, message: Message):
        search_keyword = message.text
        bi = BotInteracter(EnvParas.ROBOT_TOKEN)

        search_builder = BaseSearchBuilder()
        search_builder.keywords([search_keyword], ["name", "description"])
        es_service = ElasticService()
        resp = es_service.search(search_builder, index=[ElasticIndices.CHANNEL, ElasticIndices.GROUP])
        respBody = resp.body
        hits = respBody["hits"]
        total = hits["total"]["value"]
        hitDatum = hits["hits"]
        if total == 0:
            bi.send_message(message.from_data.id, "没有搜索到结果")
            return

        # 搜索到内容
        recommendation = "为您搜索到以下结果：\n"
        for hitData in hitDatum:
            index_name = hitData["_index"]
            data_source = hitData["_source"]
            name = data_source["name"]
            link = data_source["link"]
            member_num = data_source["member_num"]
            content_tag_str = "群组"
            if index_name == ElasticIndices.CHANNEL:
                content_tag_str = "频道"

            recommendation += f"{content_tag_str} {name}({member_num}) {link} \n"
        print("rep_text:", recommendation)

        result = bi.send_message(message.from_data.id, recommendation)
        if result:
            logger.info(f"Echo message back to {message.from_data.id} successfully")
        else:
            logger.error(
                f"Failed to send recommendation back to {message.from_data.id}"
            )
