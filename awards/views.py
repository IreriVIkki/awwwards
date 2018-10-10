from django.shortcuts import HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404
from django.core.mail import mail_admins
from django.contrib.auth.models import User
from django.contrib import auth
import datetime

# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('user_details')

        # else:
        #     messages.error(request, 'Error wrong username/password')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    return render(request, 'profile.html', {'user': user})
