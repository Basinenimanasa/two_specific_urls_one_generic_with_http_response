from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def dhoni(request):
    return render(request,'dhoni.html')
def jadeja(request):
    return HttpResponse('<h1> he is the match of the man</h1>')