from django.urls import path
from . import views

urlpatterns = [
    path("",views.index ,name="index"),
    path("weather/",views.weather , name="weather"),
    path("go_home/" , views.goHome ,name="go_home" ),
    path("hava_durumu/", views.havaDurumu ,name="hava_durmu")
]