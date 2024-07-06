# TeleSearchBot
An intelligent robot for people to search on Telegram.

# Plan
1. build up a robot for content search
2. import adsgram into the robot
3. fix bugs and enhance the robot

# Design
![bot_plan](https://github.com/hunter2009pf/TeleSearchBot/assets/32154029/4ac387b5-9569-4480-a28b-279b58050367)


# Log
1. use API interface to get group ID, the returned message looks like this:
```
{
	"ok": true,
	"result": [{
		"update_id": 212274839,
		"message": {
			"message_id": 4,
			"from": {
				"id": <message sender ID>,
				"is_bot": false,
				"first_name": "Kim",
				"last_name": "Joohn",
				"language_code": "zh-hans"
			},
			"chat": {
				"id": <group_id>,
				"title": "game fans",
				"type": "supergroup"
			},
			"date": 1720090140,
			"text": "/haha @<robot name>",
			"entities": [{
				"offset": 0,
				"length": 5,
				"type": "bot_command"
			}, {
				"offset": 6,
				"length": 16,
				"type": "mention"
			}]
		}
	}]
}
```
2. we can setup webhook to accept messages received by Telebots
API: https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}

# Problems
1. got an error when create telegram application
solution: https://github.com/tdlib/telegram-bot-api/issues/273

# References
1. TON: https://github.com/ton-blockchain/ton
2. TON documents: https://docs.ton.org/
3. Telegram bots: https://core.telegram.org/bots
4. Method of creating bots: https://www.kyzy.cc/350.html
5. Sending messages to bots: https://blog.csdn.net/tz_zs/article/details/127110582
6. Keeping critical info: https://www.bilibili.com/video/BV1Vj42197kj/?spm_id_from=333.999.0.0&vd_source=c2c36667f866bcdc49a4a305213efb64
7. Telethon: https://github.com/LonamiWebs/Telethon
8. Webhook: https://cloud.tencent.com/developer/ask/sof/104354741
9. Elastic Search: https://www.elastic.co/cn/what-is/vector-search
10. AdsGram: https://adsgram.ai/
