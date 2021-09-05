"""Users views"""

# Django
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Models
from django.contrib.auth.models import User
from users.models import Profile

#Exceptions
from django.db.utils import IntegrityError
# Create your views here.

@login_required
def update_profile(request):
    """Update a users profile view."""
    
    return render(request, 'users/update_profile.html')

def login_view(request):
    # import pdb
    # pdb.set_trace()
    # https://docs.djangoproject.com/en/3.2/topics/auth/default/#auth-web-requests
    
    """Login view"""
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', context={'error':'Invalid username or password'})
            
    return render(request, 'users/login.html')

def signup(request):
    """Signup view"""
    if request.method == 'POST':
        
        username = request.POST['username']
        passwd = request.POST.get('passwd', True)
        passwd_confirmation = request.POST.get('passwd_confirmation', True)
        
        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error':'Password confirmation does not match.'})
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error':'Username is already taken.'})
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
        profile = Profile(user=user)
        profile.save()
        
        return redirect('login')
    
    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')