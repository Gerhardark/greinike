from django.urls import path
from django.http import HttpResponse

def hello (requests):
    return HttpResponse("hola mundo")

urlpatterns = [
    path("", hello)
]