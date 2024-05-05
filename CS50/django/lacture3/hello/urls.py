from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("nini", views.nini, name="nini"),
    path("david", views.david, name="david")
]