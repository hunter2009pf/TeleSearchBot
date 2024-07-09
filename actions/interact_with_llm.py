from abc import ABC, abstractmethod
from openai import OpenAI
import openai

from config.env_paras import EnvParas
from utils.log_util import logger


class LargeLanguageModel(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass


class KimiChat(LargeLanguageModel):
    def __init__(self, session_id: int, is_group: bool = False):
        self.session_id = session_id
        self.is_group = is_group
        self.client = OpenAI(
            api_key=EnvParas.KIMI_API_KEY,
            base_url="https://api.moonshot.cn/v1",
        )

    def generate_response(self, prompt: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                model="moonshot-v1-8k",
                messages=[
                    {
                        "role": "system",
                        "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
            )
        except openai.RateLimitError as e:
            logger.error(f"kimi reaches its query rate limit: {e}")
            return "大语言模型调用过快，请稍后再试"
        if len(completion.choices) == 0:
            return "大语言模型无法回答这个问题"
        else:
            logger.info(completion.choices[0].message.content)
            return completion.choices[0].message.content
