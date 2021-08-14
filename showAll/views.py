from django.shortcuts import render

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

def getDocId(email):
    collRef=db.collection('Profiles').where('email','==',email).stream()
    docId=None
    for doc in collRef:
        docId=doc.id
        break
    return docId


def showAll(request):
    email=request.session.get('email')
    docId=getDocId(email)
    collRef1=db.collection('UserAddedPeople').document(docId).collection('AddedPeople').where('days_left','==',0).stream()
    todayList=[]
    for doc in collRef1:
        data=doc.to_dict()
        print(data)
        todayList.append(data)

    collRef2=db.collection('UserAddedPeople').document(docId).collection('AddedPeople').where('days_left','>',0).stream()
    laterList=[]
    for doc in collRef2:
        data=doc.to_dict()
        print(data)
        laterList.append(data)

    context={'todayList':todayList,'laterList':laterList,'message':'Hello there!'}
    print(context)
    return render(request,'showAll.html',context=context)
