from django.shortcuts import render
from django.http import HttpResponse 
from django.urls import reverse
# Create your views here.

def main_page(request):
    return render(request , "my_app/main_page.html")
def second_page(request):
    return render(request , "my_app/second_page.html" )
