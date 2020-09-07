from django.shortcuts import render, redirect
from web_auth.models import Chat, Message
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .forms import MessageForm


# Create your views here.


@login_required(login_url='/auth/login/')
def chat_list(request):
    chats = Chat.objects.filter(members__in=[request.user.id])
    user = request.user
    return render(request, 'chat/chatlist.html', {
        'chats': chats,
        'user': user,
    })


def chat_view(request, pk):
    try:
        chat = Chat.objects.get(id=pk)
        if request.user in chat.members.all():
            messages = Message.objects.filter(chat=chat)
        else:
            return HttpResponse('You have no access to this chat !')
    except Chat.DoesNotExist:
        return HttpResponse('Chat does not exist !')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.chat = chat
            message.save()
            return redirect('/chat/'+str(chat.pk))
    else:
        form = MessageForm
        return render(request, 'chat/chatview.html', {
            'messages': messages,
            'form': form,
        })


def join_chat(request, pk):
    User = get_user_model()
    user = User.objects.get(pk=pk)
    chats = Chat.objects.all()
    for chat in chats:
        if request.user and user in chat.members.all() and user and request.user in chat.members.all():
            return redirect('/chat/'+str(chat.pk))

    chat = Chat.objects.create()
    chat.members.add(request.user)
    chat.members.add(pk)
    return redirect('/chat/'+str(chat.pk))