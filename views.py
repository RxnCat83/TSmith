from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()


    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, "There was an error with your login. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})




def customer_lead(request, pk):
    if request.user.is_authenticated:
        # Lookup record
        customer_lead = get_object_or_404(Record, id=pk)
        return render(request, 'leads.html', {'customer_lead': customer_lead})
    else:
        messages.error(request, "You must be logged in to view this lead.")
        return redirect('home')

    
#def add_customer_lead(request, pk):
    if request.user.is_authenticated:
        # Lookup record
        add_customer_lead = get_object_or_404(Record, id=pk)
        return render(request, 'user.html', {'add_customer_lead': add_customer_lead})
    else:
        messages.error(request, "You must be logged in to view this lead.")
        return redirect('home')

#
# Only the Administrator can delete the customer leads from the backend. 