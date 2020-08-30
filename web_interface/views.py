from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/auth/login/')
def profile(request):
    user = request.user
    print(user.email)
    return render(request, 'profile.html', {
        'user': user
    })