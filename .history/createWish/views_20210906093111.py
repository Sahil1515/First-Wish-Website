from django.shortcuts import render

# Create your views here.


def createwish(request):
    return render(request, 'create_wish')