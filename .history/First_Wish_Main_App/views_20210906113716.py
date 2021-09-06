from django.shortcuts import render

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

from django.shortcuts import redirect

import datetime
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



if not firebase_admin._apps:
    cred = credentials.Certificate('file.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()



def send_mail_to_user_about_his_added_person_birthday(receiver_email,data):
    print("send_mail_to_user_about_his_added_person_birthday")
    sender_email = os.environ.get("SENDER_EMAIL")
    password = os.environ.get("SENDER_PASS")

    message = MIMEMultipart("alternative")
    message["Subject"] = "First Wish Contact"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    html = """\
    <html>

    <body>
        <p> Hey,</p>
        <p>Its {0} {1}'s Happy Birthday today. Bless them with your wishes. Remember earlier wishes have no match. </p>
        <p>You may consider creating wishes on <b>First Wish</b>.</p>
        First Wish
    </body>
    </html>
    """.format(data['fname'],data['lname'])

    part2 = MIMEText(html, "html")

    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )



def getMail(main_doc):
    data=db.collection('Profiles').document(main_doc.id).get()
    print(data['email'])
    return data['email']


def decrease_day_count_and_send_bday_mails():
    print("\ndecrease_day_count_and_send_bday_mails\n")
    MainCollUserAddedPeople=db.collection('UserAddedPeople').get()
    print(MainCollUserAddedPeople)

    for main_doc in MainCollUserAddedPeople:
        print(main_doc.id)
        email=getMail(main_doc)
        InnerCollUserAddedPeople=db.collection('UserAddedPeople').document(main_doc.id).collection('AddedPeople').stream()
        for doc in InnerCollUserAddedPeople:
            data=doc.to_dict()
            print(data)
            data=data['days_left']-1
            if data['days_left']==0:
                send_mail_to_user_about_his_added_person_birthday(email,data)
            db.collection('UserAddedPeople').document(main_doc.id).collection('AddedPeople').document(doc.id).update(data)




def index(request):
    if 'email' not in request.session and 'username' not in request.session:
        return redirect('/login')
    return render(request, 'index.html')





# yes , a process could have more that one socket
#  (combination of ip address and port address)
#  but at a particular instance of time it can be only one..