from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("Já existe")

        user = User.objects.create_user(username=username, email=email, password=password)  
        user.save()   

        return render(request, 'login.html')
    

    


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user:
            login_django(request, user)
            return HttpResponse("LOGADO")
        else:
             return HttpResponse("email ou senha invalido")

@login_required(login_url="login/")
def plataforma(request):
        return HttpResponse("ola deu boa")
  
