from django.shortcuts import render
from django.core.mail import send_mail


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