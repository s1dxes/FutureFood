from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import auth, messages
from django.urls import reverse
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserCreationForm
from home.models import Basket
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! you have successfully registered!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user,data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! you have successfully changed the data!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    context = {'titile': 'Store-Profile',
               'form': form,
               'baskets': Basket.objects.filter(user = request.user),
}
    return render(request, 'users/profile.html', context)

def bmi_history(request):
    user = User.objects.get(username=request.user.username,)
    id = User.objects.get(id = request.user.id)
    return render(request, 'users/bmi_history.html', {'user': user, 'id': id})


