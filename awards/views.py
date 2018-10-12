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
    post = Post.objects.first()
    posts = Post.objects.all()
    print(posts)

    average_usability = Rating.average_usability(post)
    average_design = Rating.average_design(post)
    average_creativity = Rating.average_creativity(post)
    average_content = Rating.average_content(post)
    average_mobile = Rating.average_mobile(post)
    average_rating = Rating.average_rating(post)
    context = {
        'posts': posts,
        'post': post,
        'average_usability_w': stringify_rating(average_usability)[0],     'average_usability_d': stringify_rating(average_usability)[1],
        'average_design_w': stringify_rating(average_design)[0],           'average_design_d': stringify_rating(average_design)[1],
        'average_creativity_w': stringify_rating(average_creativity)[0],   'average_creativity_d': stringify_rating(average_creativity)[1],
        'average_content_w': stringify_rating(average_content)[0],         'average_content_d': stringify_rating(average_content)[1],
        'average_mobile_w': stringify_rating(average_mobile)[0],           'average_mobile_d': stringify_rating(average_mobile)[1],
        'average_rating': average_rating,
    }
    return render(request, 'index.html', context)


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


def other_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if not request.user.is_authenticated():
        return redirect("login")
    try:
        profile = user.profile
    except:
        return redirect('edit_profile')

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
    user = request.user
    post = Post.objects.get(pk=post_id)
    post_reviews = Rating.objects.filter(post=post)
    judges = list(set([judge.user for judge in post_reviews]))
    if request.user.is_authenticated:
        print(post_id)
        p_user = post.uploaded_by
        if request.method == 'POST':
            rf = RatePostForm(request.POST)
            cf = ReviewCommentForm(request.POST)
            print(rf.is_valid())
            print(cf.is_valid())
            if rf.is_valid():
                rf.save()
                rating = Rating.objects.last()
                rating.user = user
                rating.post = post
                rating.save()
            if cf.is_valid():
                cf.save()
                review = Comment.objects.last()
                review.author = user
                review.post = post
                review.save()
            return redirect(reverse('profile'))
        else:
            rf = RatePostForm()
            cf = ReviewCommentForm()
        print(judges)

        average_usability = Rating.average_usability(post)
        average_design = Rating.average_design(post)
        average_creativity = Rating.average_creativity(post)
        average_content = Rating.average_content(post)
        average_mobile = Rating.average_mobile(post)
        average_rating = Rating.average_rating(post)
        context = {
            'average_usability_w': stringify_rating(average_usability)[0],       'average_usability_d': stringify_rating(average_usability)[1],
            'average_design_w': stringify_rating(average_design)[0],            'average_design_d': stringify_rating(average_design)[1],
            'average_creativity_w': stringify_rating(average_creativity)[0],     'average_creativity_d': stringify_rating(average_creativity)[1],
            'average_content_w': stringify_rating(average_content)[0],           'average_content_d': stringify_rating(average_content)[1],
            'average_mobile_w': stringify_rating(average_mobile)[0],            'average_mobile_d': stringify_rating(average_mobile)[1],
            'average_rating': average_rating,
            'rf_form': rf,
            'cf_form': cf,
            'p_user': p_user,
            'user': user,
            'post': post,
            'judges': judges
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


def stringify_rating(rating):
    r = str(rating).split('.')
    x = r[1]
    if len(r[1]) < 2:
        x += '0'

    return [r[0], x]
