from django.urls import path
from chat.consumers import SocketConsumer
from chat.views import one_on_one_chat

web_socket_url_patterns = [path("", SocketConsumer.as_asgi())]

urlpatterns = [
    path("", one_on_one_chat),
]
