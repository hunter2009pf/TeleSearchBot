from enum import Enum


class Constants:
    SERVICE_NAME = "Telegram Search Robot"
    VERSION = "0.0.1"
    ENVIRONMENT_FILE_NAME = "config.env"
    DEFAULT_OFFSET = -1
    DEFAULT_ROUND_QUERY_TIEM_INTERVAL_IN_SECONDS = 6
    KEYWORD_MAX_LENGTH = 16


class ResponseCodes:
    OK = 0
    ERROR = 100


class TaskTypes(Enum):
    DO_NOTHING = 0
    ASK_CHATGPT = 1
    SEARCH_KEYWORD = 2
