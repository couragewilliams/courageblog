import email
from django.http import request
from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserUpadteForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Posts
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            subject=f"welcome {username}"
            message = 'thanks for joining courage blog'
            email = form.cleaned_data.get('email')
            send_mail(subject,message, settings.EMAIL_HOST_USER, [email])
            messages.success(request,f'Welcome {username}')
            return redirect('login')

    else:
        form=UserRegisterForm()
    return render(request,'user/register.html',
                  {'form': form})
    
@login_required
def profile(request):
    post=Posts.objects.filter(author=request.user)
    if request.method == 'POST':
        user_form=UserUpadteForm(request.POST, instance=request.user)
        profile_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Update Successful')
            return redirect('profile')
    else:
        user_form=UserUpadteForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
    context={'user_form':user_form, 'profile_form':profile_form, 'post':post}
    return render(request,'user/profile.html', context)