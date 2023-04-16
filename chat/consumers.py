import json
from channels.generic.websocket import AsyncWebsocketConsumer


class SocketConsumer(AsyncWebsocketConsumer):
    group_name_chat = "hittu-akky"
    group_name_notification = "notifications"

    async def connect(self):
        print(self.scope)
        await self.channel_layer.group_add(self.group_name_chat, self.channel_name)
        await self.channel_layer.group_add(self.group_name_notification, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name_chat, self.channel_name)
        await self.channel_layer.group_discard(self.group_name_notification, self.channel_name)


    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message_text"]
        user_id = text_data_json["user_id"]

        await self.channel_layer.group_send(
            self.group_name_chat,
            {"type": "chat.message", "message_text": message, "user_id": user_id},
        )
        await self.channel_layer.group_send(
            self.group_name_notification,
            {"type": "notification", "message_text": message, "user_id": user_id},
        )

    async def chat_message(self, event):
        message = event["message_text"]
        user_id = event["user_id"]
        await self.send(
            text_data=json.dumps(
                {
                    "type": "chat.message",
                    "message_text": message,
                    "user_id": user_id,
                }
            )
        )
