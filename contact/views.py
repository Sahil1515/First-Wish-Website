from django.shortcuts import render


import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.http.response import HttpResponse

# Create your views here.

def contact(request):
    return render(request, 'contact.html')


def send_mail(name,number, email,message_user):
    print("\n\n\n")
    print(name)
    print(number)
    print(email)
    print(message_user)
    print("\n\n\n")

    sender_email = os.environ.get("SENDER_EMAIL")
    receiver_email = 'sahilsaini51671@gmail.com'
    password = os.environ.get("SENDER_PASS")

    message = MIMEMultipart("alternative")
    message["Subject"] = "First Wish Contact"
    message["From"] = sender_email
    message["To"] = 'sahilsaini51671@gmail.com'

    # Create the plain-text and HTML version of your message
    html = """\
    <html>

    <body>
        <p> Hey,</p>
        <p>Name: {0}</p>
        <p>Email: {1}</p>
        <p>Number: {2}</p>
        <p>Message:  {3} </p>
        First Wish
    </body>
    </html>
    """.format(name, email,number,message_user)

    part2 = MIMEText(html, "html")

    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def send_mail_by_user(request):
    print("send_mail_by_user\n")

    print("\n\n\n")
    print(request.POST)
    print("\n\n\n")

    name =         request.POST.get('name')
    number =       request.POST.get('number')
    email =        request.POST.get('email')
    message_user = request.POST.get('msg')

    # mail code here
    send_mail(name,number, email,message_user)

    print("mail sent!\n")

    return HttpResponse(True)


# OTP Part code ends here\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# Hello Sahil! This website is awesome. I just love it!