from django.shortcuts import render

import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

from django.shortcuts import redirect

import datetime
import os

if not firebase_admin._apps:
    cred = credentials.Certificate('file.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()


def addToDatabase(request):
    fname="Sahil"
    lname="Saini"
    check="0"
    if request.method=='POST':
        fname=request.POST['getFirstName']
        lname=request.POST['getLastName']
        date=request.POST['date']
        check=request.POST['dataAboutPage']
        print(check)
        data={
            "fname": fname,
            "lname": lname,
            'date':date
        }
        if(check!="1"):
            db.collection("BirthdayReminder").document().set(data)

    return render(request, 'personAdded.html', context=data)


def birthday(request):
    arr=[]

    if request.method=='POST':
        date=request.POST['Search']
        print(date)
        colRef=db.collection("BirthdayReminder").where('date','==',date).stream()
        for doc in colRef:
            print("Hi")
            fname=doc.to_dict()['fname']
            lname=doc.to_dict()['lname']
            arr.append( fname+' '+lname)
        print(arr)
    return render(request,'birthday.html',context={'nameList':arr, 'date':date})

# def addPerson(request):
#     return render(request, 'addPerson.html', context=None)


def getNames(request):
    fnameListDatabase=[]
    lnameListDatabase=[]
    
    for doc in db.collection("BirthdayReminder").stream():
        try:
            fnameListDatabase.append(doc.to_dict()['fname'])
            lnameListDatabase.append(doc.to_dict()['lname'])
        except:
            pass

    nameListDatabase=[]

    for i in range(len(fnameListDatabase)):
        nameListDatabase.append(fnameListDatabase[i]+" "+lnameListDatabase[i])

    context={"nameList":nameListDatabase}

    return render(request, 'index.html', context=context)


def index(request):
    if 'email' not in request.session and 'username' not in request.session:
        return redirect('/login')

    date=str(datetime.datetime.now())[:10]
    print(date)
    arr=[]
    colRef=db.collection("BirthdayReminder").where('date','==',date).stream()
    for doc in colRef:
        print("Hi")
        fname=doc.to_dict()['fname']
        lname=doc.to_dict()['lname']
        arr.append( fname+' '+lname)
    return render(request, 'index.html', context={'nameList':arr})
