from django.shortcuts import render

# Create your views here.

def gifts(request):
    return render(request,'try_gifts.html')
