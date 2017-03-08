from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def dashboard(request):

    user = User.objects.get(id=request.session["user_id"])
    context = {
    "user":User.objects.get(id=request.session["user_id"]),
    }
    return render(request,'main/dashboard.html',context)


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
    else:
         messages.warning(request,'Invalid credentials. Check for valid email or long enough password')
    return redirect("/")



def logout(request):
    request.session.clear()
    return redirect("/")
