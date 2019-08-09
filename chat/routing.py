# chat/routing.py
from django.conf.urls import re_path
from django.urls import path
from .consumers import ChatConsumerInput, ChatConsumerOutput

websocket_urlpatterns = [
    #re_path(r'^ws/chat/(?P<room_name>[^/]+)/$',  ChatConsumer),
    re_path(r'^ws/chat/input/$', ChatConsumerInput),
    re_path(r'^ws/chat/output/$', ChatConsumerOutput),


]