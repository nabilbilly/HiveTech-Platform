import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async
from Teamworkspace.models import Team

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.team_slug = self.scope['url_route']['kwargs']['team_slug']
        self.room_group_name = f'team_{self.team_slug}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # Save message to the database asynchronously
        await self.save_message(username, message)

        # Send message to WebSocket group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            })

    @sync_to_async
    def save_message(self, username, message):
        from .models import Message
        user = User.objects.get(username=username)
        team = Team.objects.get(slug=self.team_slug)
        Message.objects.create(user=user, team=team, content=message)

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"message": message, "username": username}))


# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from django.contrib.auth.models import User
# from asgiref.sync import sync_to_async

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.roomGroupName = "group_chat_gfg"
#         await self.channel_layer.group_add(
#             self.roomGroupName,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.roomGroupName,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         username = text_data_json["username"]

#         # Save message to the database asynchronously
#         await self.save_message(username, message)

#         # Send message to WebSocket group
#         await self.channel_layer.group_send(
#             self.roomGroupName, {
#                 "type": "sendMessage",
#                 "message": message,
#                 "username": username,
#             })

#     @sync_to_async
#     def save_message(self, username, message):
#         from .models import Message
#         user = User.objects.get(username=username)
#         Message.objects.create(user=user, room=self.roomGroupName, content=message)

#     async def sendMessage(self, event):
#         message = event["message"]
#         username = event["username"]
#         await self.send(text_data=json.dumps({"message": message, "username": username}))
