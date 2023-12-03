from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request , "template_app/chickens.html")
def weather(request):
    return render(request , "template_app/links_htmş_uedm.html")
def goHome(request):
    return render(request , "template_app/index.html")
def havaDurumu(request):
    hava_durum_raporu = {"istanbul":30,"ankara":25,"seydisehir":10 , "manisa":200 ,"konya":[12,33,4,4,44,5555,66],"user_premium":True}
    return render(request , "template_app/hava.html" , context=hava_durum_raporu)