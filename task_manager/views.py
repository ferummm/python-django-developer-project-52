from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')
    
def ind(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })