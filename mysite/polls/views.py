# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import datetime
#
# def hello_view(request):
#     return render(request, 'hello_django.html', {
#         'data': 'Hello Django'
#     })

from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django!")


def hello2(request, username):
    return HttpResponse("Hello " + username)


def hello3(request, username):
    now = datetime.now()
    return render(request, "hello_django.html", {
        'data': 'Hello Django ' + username + ', Time:'+str(now)}, )


def add(request, a, b):
    c = a + b
    return HttpResponse(str(c))