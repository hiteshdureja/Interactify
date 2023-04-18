import json
from channels.generic.websocket import AsyncWebsocketConsumer


class SocketConsumer(AsyncWebsocketConsumer):
    group_name_chat = "-"
    group_name_notification = "notifications"

    async def connect(self):
        recipient = self.scope.get("session", {}).get("recipient")
        sender = self.scope.get("session", {}).get("user_id")
        if sender and recipient:
            users = [sender, recipient]
            users.sort()
            self.group_name_chat = self.group_name_chat.join(
                users,
            )
            if self.group_name_chat:
                await self.channel_layer.group_add(
                    self.group_name_chat, self.channel_name
                )
        await self.channel_layer.group_add(
            self.group_name_notification, self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name_chat, self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name_notification, self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        grp_type = text_data_json["type"]
        if grp_type == "chat.message":
            await self.channel_layer.group_send(self.group_name_chat, text_data_json)
        else:
            sender = self.scope.get("session", {}).get("user_id")
            text_data_json["user_id"] = sender
            await self.channel_layer.group_send(
                self.group_name_notification, text_data_json
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def notification_message(self, event):
        logged_in_user_id = self.scope.get("session", {}).get("user_id")
        sender_user_id = event.get("user_id")
        if logged_in_user_id != sender_user_id:
            await self.send(text_data=json.dumps(event))
