from django.urls import path
from . import views

urlpatterns = [
    path('',  views.chat_list, name='chatlist_view'),
    path('<int:pk>',  views.chat_view, name='chat_view'),
    path('join/<int:pk>',  views.join_chat, name='join_chat_view'),
]