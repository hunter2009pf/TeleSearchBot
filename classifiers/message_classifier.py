import re
from constants.constants import Constants, TaskTypes


class MessageClassifier:
    """A classifier for messages."""

    @classmethod
    def __contains_punctuation(cls, text: str):
        # 定义中文标点符号的正则表达式
        chinese_punctuation_pattern = r"[\u3000\u3001\u3002\uFF0C\uFF0E\u2022\uFF01\uFF1F\uFF08\uFF09\u3010\u3011\uFF0B\uFF1B\uFF1A\uFF0C\uFF1C\u201C\u201D\u300E\u300F\u2018\u2019\u201C\u201D\u300C\u300D\uFF5C\u2026]"
        # 定义英文标点符号的正则表达式
        english_punctuation_pattern = r'[.,!?;:"\'(){}]'

        # 检查中文标点符号
        if re.search(chinese_punctuation_pattern, text):
            return True

        # 检查英文标点符号
        if re.search(english_punctuation_pattern, text):
            return True

        return False

    @classmethod
    def __end_with_special_characters(
        cls, text: str, question_words=["呢", "吗", "啊"]
    ):
        # 转换为统一的字符编码，这里以utf-8为例
        sentence = text.encode("utf-8").decode("utf-8")
        # 检查句子是否以疑问词结尾
        for word in question_words:
            if sentence.endswith(word):
                return True
        return False

    @classmethod
    def classify(cls, text: str) -> TaskTypes:
        original_text = text.strip()
        length = len(original_text)
        if length == 0:
            return TaskTypes.DO_NOTHING
        elif cls.__contains_punctuation(text):
            return TaskTypes.ASK_CHATGPT
        elif cls.__end_with_special_characters(text):
            return TaskTypes.ASK_CHATGPT
        elif length < Constants.KEYWORD_MAX_LENGTH:
            return TaskTypes.SEARCH_KEYWORD
        else:
            return TaskTypes.ASK_CHATGPT
