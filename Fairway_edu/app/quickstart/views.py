from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login  as auth_login, login
from django.contrib import messages
from .forms import ConsultantSignUpForm,ConsultantLoginForm,CourseForm
from .models import *
from django.contrib.auth.decorators import login_required


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
                return redirect('dashboard')  # Redirect to the dashboard or another page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            # Print form errors for debugging
            print("Form errors:", form.errors)
            messages.error(request, 'Form is not valid.')
    else:
        form = ConsultantLoginForm()

    return render(request, 'login.html', {'form': form})

def course_list(request):
    courses = Course.objects.filter(consultant=request.user)
    user = request.user
    return render(request, 'course/course_list.html', {'courses': courses})

@login_required
def dashboard(request):
    # Extract the logged-in user's details
    user = request.user
    username = user.username
    email = user.email
    courses = Course.objects.filter(consultant=user)
    

    context = {
        'username': username,
        'email': email,
        'courses': courses
    }
    return render(request, 'dashboard.html', context)

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.consultant = request.user
            course.save()
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'course/course_form.html', {'form': form})

@login_required
def c_delete(request):
     # Extract the logged-in user's details
    user = request.user
    username = user.username
    email = user.email
    courses = Course.objects.filter(consultant=user)
    

    context = {
        'username': username,
        'email': email,
        'courses': courses
    }
    return render(request, 'course/c_delete.html', context)


@login_required
def delete_course(request, id):
    course = Course.objects.filter(consultant=request.user, pk=id)
    
    if request.method == 'POST':
        course.delete()
        return redirect('dashboard')  # Redirect to dashboard or another appropriate page
    
    return render(request, 'course/course_delete.html', {'course': course})

