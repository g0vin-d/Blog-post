from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def signup(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('loginPage')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form':form})

def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['passwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            print ("user doen't exist")
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('blog:home')