from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password, check_password
from . import models

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handlelogin(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        f_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        cipher = make_password(password)

        userObj = models.User(full_name=f_name, 
                                email=email, 
                                password=cipher)
        userObj.save()

        user = models.User.objects.get(email=email)
        context = {
            'username':user.full_name
        }
        return render(request, 'home.html', context)


    return render(request, 'create_account.html')