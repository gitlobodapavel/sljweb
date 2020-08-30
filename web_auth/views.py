from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import get_user_model

from .forms import SignupForm, LoginForm
from .tokens import account_activation_token

# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print('User saved !')
            current_site = get_current_site(request)
            mail_subject = 'Activate your SLJ account.'
            message = render_to_string('auth/email/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            print('Sending email...')
            email.send()
            print('Email sent !')

            return redirect('/')
    else:
        form = SignupForm
        return render(request, 'auth/registration.html', {
            'signup_form': form,
        })


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = form['email'].value()
        password = form['password'].value()
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('/auth/login/')
    else:
        form = LoginForm
        return render(request, 'auth/login.html', {
            'login_form': form
        })


def logout(request):
    auth.logout(request)
    return render(request, 'auth/logout.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        User = get_user_model()
        user = User.objects.get(pk=uid)
        print(user)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')