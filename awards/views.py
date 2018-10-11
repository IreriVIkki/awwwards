from django.shortcuts import HttpResponse, render, redirect, get_object_or_404, reverse, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import mail_admins
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import *
from .models import *
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
            return redirect('home')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    if not request.user.is_authenticated():
        return redirect("login")
    try:
        profile = user.profile
    except:
        return redirect('edit_profile')

    user = User.objects.get(pk=user.id)
    posts = user.posts.all()
    context = {
        'user': user,
        'posts': posts,
        'profile': profile
    }
    return render(request, 'profile.html', context)


def signup(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            print('here')
            form.save()
            return redirect('login')

    form = MyRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def post_website(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            pf = WebsitePostForm(request.POST, request.FILES)
            lf = LocationForm(request.POST)
            print(pf.is_valid())
            print(lf.is_valid())
            if pf.is_valid() and lf.is_valid():
                lf.save()
                location = Location.objects.last()
                pf.save()
                post = Post.objects.last()
                post.save_post(user)
                post.uploaded_from = location
                print('4estyguhbijnokl')
                return redirect('profile')
        else:
            pf = WebsitePostForm()
            lf = LocationForm()

        context = {
            'lf_form': lf,
            'pf_form': pf
        }
        return render(request, 'new_upload.html', context)
    return redirect('home')


def rate_website(request, post_id):
    if request.user.is_authenticated:
        user = request.user
        post = Post.get_one_post(post_id)
        p_user = post.uploaded_by
        if request.method == 'POST':
            rf = RatePostForm(request.POST)
            print(rf.is_valid())
            if rf.is_valid():
                rf.save()
                rating = Rating.get_last_post()
                rating.user = user
                rating.post = post1
                rating.save()
                return redirect('home')
        else:
            rf = RatePostForm()

        context = {
            'rf_form': rf,
            'p_user': p_user,
            'user': user
        }
        return render(request, 'rate.html', context)
    return redirect('home')


def edit_profile(request):
    form = ProfileForm()
    ad_form = AddressForm()
    user = request.user
    if request.user.is_authenticated():
        if request.method == "POST":
            try:
                profile = user.profile
                form = ProfileForm(instance=profile)
                form = ProfileForm(
                    request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    update = form.save(commit=False)
                    update.user = user
                    update.save()
            except:
                form = ProfileForm(request.POST, request.FILES)
                print(form.is_valid())
                if form.is_valid():
                    profile = form.save(commit=False)
                    profile.save_profile(user)
            return redirect('home')
    else:
        form = ProfileForm()
        ad_form = AddressForm()

    context = {
        'form': form,
        'ad_form': ad_form,
        'user': user,
    }
    return render(request, 'profile_edit.html', context)
