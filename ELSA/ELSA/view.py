# from django.http import HttpResponse
 
# def hello(request):
#     return HttpResponse("Hello world !  ")

from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'app/hello.html', context)