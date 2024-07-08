class Urls:
    BASE_URL = "https://api.telegram.org"

    SEND_MESSAGE_URL = "/bot{}/sendMessage"  # send messages to telebot

    @classmethod
    def get_send_message_url(self, bot_token):
        return self.BASE_URL + self.SEND_MESSAGE_URL.format(bot_token)


class ToFrontendUrls:
    VERSION_URL = "/version"
    SEND_MESSAGE_URL_V1 = "/v1/robot/sendMessage"
