from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login  as auth_login, login
from django.contrib import messages
from .forms import ConsultantSignUpForm,ConsultantLoginForm,AuthenticationForm
from .models import *
from django.contrib.auth import get_user_model


# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        address = request.POST.get('address')
        email=request.POST.get('user_email')
        user_contact=request.POST.get('contact')
        study_destination=request.POST.get('study_destination')
        studyplan_date=request.POST.get('studyplan_date')
        counselling_mode=request.POST.get('counselling_mode')
        study_level=request.POST.get('study_level')

    # Send email to user
        user_subject = 'Registration Confirmation'
        user_message = f'Hi {username},\n\nThank you for registering with us!\n\nYour participation in this event has been successfully registered.'
        send_mail(user_subject, user_message, email, [email])
    
     # Change here for admin email reply.
        admin_email = 'riyashakya1920@gmail.com'  
        
        # Send email to admin
        admin_subject = 'New Member for enquiry'
        admin_message = f'New member to enquiry is registered with the details:\n\nUsername: {username}\nEmail: {email}\nContact: {user_contact}\n To destinantion: {study_destination}\nFor study level: {study_level}\n For the date: {studyplan_date}\n With the counselling mode: {counselling_mode}'
        send_mail(admin_subject, admin_message, admin_email, [admin_email])
    
    return render(request, 'index.html')

def sign_up(request):
    if request.method == 'POST':
        form = ConsultantSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to a dashboard or any other page after sign-up
    else:
        form = ConsultantSignUpForm()
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = ConsultantLoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('index')  # Redirect to the dashboard or another page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)
            messages.error(request, 'Form is not valid.')
    else:
        form = ConsultantLoginForm()

    return render(request, 'login.html', {'form': form})