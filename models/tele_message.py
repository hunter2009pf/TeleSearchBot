class TeleUser:
    @staticmethod
    def from_dict(data):
        return TeleUser(
            id=data.get("id"),
            is_bot=data.get("is_bot"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            language_code=data.get("language_code"),
        )

    def __init__(self, id, is_bot, first_name, last_name, language_code):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.language_code = language_code

    def __repr__(self):
        return (
            f"TeleUser(id={self.id}, is_bot={self.is_bot}, first_name='{self.first_name}', "
            f"last_name='{self.last_name}', language_code='{self.language_code}')"
        )


class Chat:
    @staticmethod
    def from_dict(data):
        return Chat(
            id=data.get("id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            type=data.get("type"),
        )

    def __init__(self, id, first_name, last_name, type):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.type = type

    def __repr__(self):
        return (
            f"Chat(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', "
            f"type='{self.type}')"
        )


class Message:
    @staticmethod
    def from_dict(data):
        from_user = TeleUser.from_dict(data["from"])
        chat = Chat.from_dict(data["chat"])
        return Message(
            message_id=data.get("message_id"),
            from_data=from_user,
            chat_data=chat,
            date=data.get("date"),
            text=data.get("text"),
        )

    def __init__(
        self,
        message_id: str,
        from_data: TeleUser,
        chat_data: Chat,
        date: int,
        text: str,
    ):
        self.message_id = message_id
        self.from_data = from_data
        self.chat_data = chat_data
        self.date = date
        self.text = text

    def __repr__(self):
        return (
            f"Message(message_id={self.message_id}, from_data={self.from_data}, "
            f"chat_data={self.chat_data}, date={self.date}, text={self.text})"
        )


# # 假设这是从 JSON 转换来的字典
# data = {
#     "message_id": 44,
#     "from": {
#         "id": 5340399297,
#         "is_bot": False,
#         "first_name": "Kunikimn",
#         "last_name": "Cheers",
#         "language_code": "zh-hans"
#     },
#     "chat": {
#         "id": 5340399297,
#         "first_name": "Kunikimn",
#         "last_name": "Cheers",
#         "type": "private"
#     },
#     "date": 1720523667,
#     "text": "哈哈哈哈哈"
# }

# # 使用 from_dict 方法创建 Message 实例
# message = Message.from_dict(data)

# # 打印对象信息
# print(message)
