from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def dashboard(request):
    ids = []
    num = request.session["user_id"]
    total_users_options = Friend.objects.filter(user_liked_by=request.session["user_id"])

    for friend in total_users_options:
        ids.append(friend.user_liked.id)

    revised_user_options=User.objects.exclude(id=request.session["user_id"]).exclude(id__in=ids)

    user = User.objects.get(id=request.session["user_id"])
    context = {
    "user":User.objects.get(id=request.session["user_id"]),
    "total_users": revised_user_options,
    "my_friends": Friend.objects.filter(user_liked_by=request.session["user_id"]),
    }
    return render(request,'main/dashboard.html',context)


def view_profile(request, id):
    context = {
    "user":User.objects.get(id=id)
    }
    return render(request,'main/profile.html',context)

#Views that process forms
def login(request):
    if request.method == 'POST':
        login = User.objects.login_user(request.POST)
        if login:
            request.session["user_id"] = login[1].id
            return redirect ("/dashboard")
        else:
            messages.error(request,'Invalid credentials')
    return redirect("/")

def register(request):
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
        name = request.POST.get("name"),
        alias = request.POST.get("alias"),
        date_of_birth = request.POST.get("date_of_birth"),
        email = request.POST.get("email"),
        password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
        )
        request.session["user_id"]=user.id
        return redirect("/dashboard")
    return redirect("/")

def add_friend(request, id):
    friend = Friend.objects.create(
    user_liked = User.objects.get(id=id),
    user_liked_by = User.objects.get(id=request.session["user_id"])
    )
    return redirect ("/dashboard")

def remove(request, id):
    Friend.objects.filter(user_liked=id).delete()
    return redirect("/dashboard")

def logout(request):
    request.session.clear()
    return redirect("/")
