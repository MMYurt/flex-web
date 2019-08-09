from django.urls import path, re_path

from .views import  index, room, output

app_name = 'chat'

urlpatterns=[
    path('', index, name='index'),
    #re_path(r'^(?P<room_name>[^/]+)/$', room, name='room3'),
    path('input/', room, name='room3'),
    path('output/', output, name='output'),

]