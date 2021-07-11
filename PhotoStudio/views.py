from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.conf import settings 
from .models import Appointments, Queries
from socket import gaierror, timeout
from django.contrib import messages

# Create your views here.
def index(request):
    if (request.method == "POST"):
        userName = request.POST["Name"]
        userEmail = request.POST["Email"]
        userPhno = request.POST["ContactNum"]
        userMsg = request.POST["userQuery"]
        body = f"""<div style="border: 2px solid black; padding: 1rem;"><p><b>Name : {userName}</b></p><br><p>Phone no : {userPhno}</p><hr><u><b>query</b></u><br><p>{userMsg}</p></div>"""
        subj = "Query"
        msg, status = send_email(subj, userEmail, body)
        #print(userName," ",userMsg," ",userPhno," ",userEmail)
        params = {'responce':msg, 'status':status}
        if (status=="success"):
            data = Queries.objects.create(
            User_Name= userName,
            User_Email= userEmail,
            User_Contact= userPhno,
            User_Discription= userMsg)
            data.save()
        return render(request, 'index.html', params)
    else:
        params = {}
        return render(request, 'index.html', params)

def base(request):
    return render(request, 'base.html')

def bookings(request):
    if (request.method == "POST"):
        userFirstName = request.POST["CFirstName"]
        userLastName = request.POST["CLastName"]
        userEmail = request.POST["cEmail"]
        userContact = request.POST["cContactNo"]
        BookingDate = request.POST["BookedOn"]
        apptDate = request.POST["apptDate"]
        userEvent = request.POST["cEvent"]
        userMsg = request.POST["cMessage"]

        body = f"""<div style="border: 2px solid black; padding: 1rem;"><p><u><b> User Name : {userFirstName}{userLastName} </b></u><br />User Email: {userEmail}<br />Phon No : {userContact}<br />Booked on :{BookingDate}<br />Appointment Date : {apptDate}<br />For  {userEvent} <hr><u><b>Message :</b></u>{userMsg}</p></div>"""

        subj = "Regards Booking Appointment"
        msg, status = send_email(subj, userEmail, body)
        params = {'responce':msg, 'status':status}
        if (status=="success"):
            Adata = Appointments.objects.create(User_FirstName=userFirstName,
            User_LastName= userLastName,
            User_Email= userEmail,
            User_Contact= userContact,
            User_BookedOn= BookingDate,
            User_ApptDate= apptDate,
            User_Event= userEvent,
            User_Suggestion= userMsg)
            print(status)
            Adata.save()
        print(status)
        return render(request, 'book.html', params)
    else:
        params = {}
        return render(request, 'book.html', params)

def send_email(subject, Uemail, body):
    text_content = "A mail from UkPhotography user"
    html_content = f'{body}'
    from_mail = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, text_content, from_mail, ['ukphotography2002@gmail.com'], reply_to=[Uemail,])
    msg.attach_alternative(html_content, "text/html")
    try:
        msg.send()
    except BadHeaderError:
        Msg = "Invalid header found"
        status = "error"
        return(Msg, status)
    except (gaierror, timeout):
        Msg = "SORRY!<br/>Check your internet connection or try again after some time"
        status = "error"
        return(Msg, status)
    Msg="Thank you for getting in touch!<br/>we will get back in touch with you soon!<br>Have a great day!"
    status = "success"
    return(Msg, status)