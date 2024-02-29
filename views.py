from django.shortcuts import render, redirect
# This is to create the login for users
from django.contrib.auth import authenticate, login, logout
# This will let the user know that they have successfully logged in and out. 
from django.contrib import messages



def home(request):
    # Check to see if user logs in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error with your log in. Please try again.")
            return redirect('home')
        
    else:
        return render(request, 'home.html', {})



    return render(request, 'home.html', {})

#  The log_user function below would be needed if I wanted to create a seperate login page.
# As I don't, I have will not use this funtion.
# I want the site to go directly to the user login page. 

#def login_user(request):
    #pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
