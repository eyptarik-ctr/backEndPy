from django.urls import path
from . import views #. kendi klasorunden import eder

urlpatterns = [
    path("",views.index,name="index_html")

]