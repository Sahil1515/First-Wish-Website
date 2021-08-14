import datetime
from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.

import os
import environ
from datetime import date


from firebase_admin import firestore,credentials
import firebase_admin

if not firebase_admin._apps:
    cred=credentials.Certificate(
        os.environ.get("TYPE"),
        os.environ.get("PROJECT_ID"),
        os.environ.get("PRIVATE_KEY_ID"),
        os.environ.get("PRIVATE_KEY"),
        os.environ.get("CLIENT_EMAIL"),
        os.environ.get("CLIENT_ID"),
        os.environ.get("AUTH_URI"),
        os.environ.get("TOKEN_URI"),
        os.environ.get("AUTH_PROVIDER_X509_CERT_URL"),
        os.environ.get("CLIENT_X509_CERT_URL")
    )
    firebase_admin.initialize_app(cred)
db=firestore.client()

env_path=os.path.join(os.path.dirname(__file__),'../.env')
environ.Env.read_env(env_path)



def addPerson(request):
    return render(request,'addPerson.html')


def getDocId(email):
    collRef=db.collection('Profiles').where('email','==',email).stream()
    docId=None
    for doc in collRef:
        docId=doc.id
        break
    return docId

from datetime import date

def checkLeapYear(year):
    if year%4==0:
        if year %100==0:
            if year%400==0:
                return 1
            return 0
        return 1
    return 0

def getDaysLeft(day_month):
    month1=int(day_month[0:2])
    day1=int(day_month[3:])

    current_date=date.today()
    month2=int((str(current_date))[5:7])
    day2=int((str(current_date))[8:])

    year=int((str(current_date))[0:4])

    a=date(year,month1,day1)    
    b=date(year,month2,day2)

    if a==b: 
        return 0

    days_left=str(a-b)

    days_left=int(days_left[:days_left.find(' ')])

    if days_left<0:
        if checkLeapYear(year):
            days_left=366+days_left
        else:
            days_left=365+days_left

    return days_left


def add_person_api(request):
    print("\naddPerson function\n")
    fname=request.POST['fname']
    lname=request.POST['lname']
    dob=request.POST['dob']
    relation=request.POST['relation']
    message=request.POST['message']
    day_month=dob[5:]
    days_left=getDaysLeft(day_month)

    data={
        "fname":fname,
        "lname":lname,
        "dob":dob,
        "relation":relation,
        "message":message,
        "day_month":day_month,
        'days_left':days_left
    }
    email=request.session.get('email')
    docId=getDocId(email)

    db.collection('UserAddedPeople').document(docId).collection('AddedPeople').document().set(data)
    
    print(fname,lname,dob,relation,message)

    return_data={
        "flag":True
    }
    return JsonResponse(return_data)