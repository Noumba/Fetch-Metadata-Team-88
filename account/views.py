from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
import uuid
from django.forms import PasswordInput
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import User, Profile
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .helpers import send_forget_password_mail

from django.contrib.auth.hashers import make_password


# Create your views here.

def forgot_password_view(request):
    return render(request, 'auth/forgotten_password.html')


def auth_users_view(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'auth/landing.html')
    return render(request, 'auth/login.html')


def login_view(request):
    return render(request, 'auth/login.html', )


def register_view(request):
    return render(request, 'auth/register.html', )


def register_api(request):
    try:
        if request.method == 'POST':

            print(request)
            first_name = request.POST.get("first_name")
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            rt_password = request.POST.get('rt_password')
            email = request.POST.get('email')

            print(first_name, last_name, username, password, email)

            if (username == '' or password == '' or email == '' or rt_password == '' or first_name == '' or last_name == ''):
                print('username and password are required')
                return render(request, 'auth/register.html')

            if password != rt_password:
                messages.error(request, 'Password mismatch error')
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, 'User with that username already exists')
            if User.objects.filter(email=email).exists():
                messages.error(
                    request, 'User with that email address already exists')
            print('reaching the create user method')
            user = User.objects.create(username=username, email=email,
                                       password=make_password(password), first_name=first_name, last_name=last_name)
            print('reaching the login function')
            login(request, user)
            return render(request, 'auth/landing.html',)
    except Exception as e:
        print(e)
    render(request, 'auth/register.html')


def login_api(request):
    try:
        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            messages.error(request, 'Invalid username or password')
            return redirect('/')
    except Exception as e:
        print(e)
    return render(request, 'auth/login.html')


def logout_api(request):
    try:
        logout(request,)
        return redirect('/')
    except Exception as e:
        raise e


def change_password(request, token):
    context = {}
    print(token)

    try:
        profile_obj = Profile.objects.get(
            forget_password_token=token)
        print(profile_obj)
        context = {'user_id': profile_obj.user.id}
        print(context)

        if request.method == 'POST':
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('rt_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change_password/{token}/')

            if new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change_password/{token}/')

            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login/')

    except Exception as e:
        print(e)
    return render(request, 'auth/reset_password.html', context)


def forgot_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get("username")

            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('/forgot_password/')

            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())

            # user = user_obj.id

            forget_password_token = token

            profile_obj = Profile(
                user=user_obj, forget_password_token=forget_password_token)
            profile_obj.save()
            # print("Yes message")
            send_forget_password_mail(user_obj.email, token)
            print("Yes message")
            messages.success(
                request, 'An email is sent to your email address. Please also check your SPAM Mails.')
            return redirect('/forgot_password/')

    except Exception as e:
        print(e)
    return render(request, 'auth/forgotten_password.html')
