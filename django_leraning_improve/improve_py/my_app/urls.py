from django.urls import path
from . import views


urlpatterns = [
    path("" ,views.main_page , name="main_page"),
    path("second_site" , views.second_page , name="secondPg")

]