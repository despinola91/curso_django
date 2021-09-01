"""Users views"""

# Django
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Create your views here.

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
