from django.http import HttpResponse

def index(request):
    return HttpResponse('hello, world, Youre at the polls index.')

