import json
from channels.generic.websocket import AsyncWebsocketConsumer


class SocketConsumer(AsyncWebsocketConsumer):
    group_name = "hittu-akky"

    async def connect(self):
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message_text"]
        user_id = text_data_json["user_id"]

        await self.channel_layer.group_send(
            self.group_name,
            {"type": "chat.message", "message_text": message, "user_id": user_id},
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
