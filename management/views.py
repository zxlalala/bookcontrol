from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from models import *

# Create your views here.
def index(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu':'homepage',
        'user':'user',
    }
    return render(request, 'management/index.html', content)

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password','')
        repeat_password = request.POST.get('repeat_password','')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username','')
            if User.objects.filter(username = username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username,password=password,email=request.POST.get('email',''))
                new_user.save()
                new_my_user = MyUser(user=new_user,nickname=request.POST.get('nickname',''))
                new_my_user.save()
                state = 'success'
    content = {
        'active_menu': 'homepage',
        'user': None,
        'state': state,
    }
    return render(request, 'management/signup.html', content)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu':'homepage',
        'state':state,
        'user':None,
    }
    return render(request,'management/login.html',content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password','')
        new_password = request.POST.get('new_password','')
        repeat_password = request.POST.get('repeat_password','')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
    else:
        state = 'pasword_error'
    content = {
        'active_menu':'homepage',
        'state':state,
        'user':user,
    }
    return render(request,'management/set_password.html',content)


def permission_check(user):
    if user.is_authenticated():
        return user.myuser.permission > 1
    else:
        return FalseUser


@user_passes_test(permission_check)
def add_book(request):
    user = request.user
    state = None
    if request.method == 'POST':
        new_book = Book(
            title = request.POST.get('title', ''),
            author = request.POST.get('author', ''),
            price = request.POST.get('price',0),
            publish_date = request.POST.get('publish_date','')
        )
        new_book.save()
        state = 'success'
    content = {
        'active_menu': 'add_book',
        'user': user,
        'state': state,
    }
    return render(request, 'management/add_book.html',content)



def add_img():
    pass
def view_book_list():
    pass

def detail():
    pass




