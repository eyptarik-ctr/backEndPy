from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"my_app2/index.html")
