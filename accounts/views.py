from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('reviews:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'reviews:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'accounts/detail.html', context)

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)

def password_update(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:detail', request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/password_update.html', context)

def delete(request):
    if request.method == "POST":
        request.user.delete()
        auth_logout(request)
        return redirect('accounts:login')

def follow(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.user != user:
        if request.user.followings.filter(id=user.pk).exists():
            request.user.followings.remove(user)
        else:
            request.user.followings.add(user)
    return redirect('accounts:detail', pk)