from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from verify_email import send_verification_email
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from home.models.category import Category
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)  # for email verification
            # inactive_user.cleaned_data['email']     # for email verification
            # form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('verify')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def verify(request):
    return render(request, 'users/verify.html')


####################
# class UserEditView(generic.CreateView):
#     form_class = UserChangeForm
#     template_name = "users/edit_profile.html"
#     success_url = reverse_lazy('home')
#
#     def get_object(self):
#         return self.request.user
####################

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    categories = Category.objects.all()
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'categories': categories
    }

    return render(request, 'users/profile.html', context)
