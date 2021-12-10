from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Feature

# Create your views here.
def index(request):
    # name= 'John'
    # we create  a dictionary so that we can add more files
    # lets create a dictonary called context and add aall our data therer
    # context = {
    #     'name':'PATRICK',
    #     'age':'21',
    #     'nationality':'kenyan'
    # }
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if requestmethod == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'CredentialS Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def counter(request):
    # this gets the words from the name of the form in the
    # if e change the name of the text are , we have o change the variable as well
    word = request.GET['words']
    amount_of_words = len(word.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
