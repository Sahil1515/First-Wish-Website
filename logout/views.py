from django.shortcuts import redirect, render

from Login.forms import loginPage
# Create your views here.


def logout(request):

    form =loginPage()

    try:
        del request.session['email']
        del request.session['username']
    except:
        pass
    return redirect('http://localhost:8000/login')
    
