class Urls:
    BASE_URL = "https://api.telegram.org"

    SEND_MESSAGE_URL = "/bot{}/sendMessage"  # send messages to telebot
    GET_UPDATES_URL = "/bot{API_TOKEN}/getUpdates"  # get updates from telebot

    @classmethod
    def get_send_message_url(self, bot_token):
        return self.BASE_URL + self.SEND_MESSAGE_URL.format(bot_token)

    @classmethod
    def get_get_updates_url(self, bot_token):
        return self.BASE_URL + self.GET_UPDATES_URL.format(API_TOKEN=bot_token)


class ToFrontendUrls:
    VERSION_URL = "/version"
    SEND_MESSAGE_URL_V1 = "/v1/robot/sendMessage"
