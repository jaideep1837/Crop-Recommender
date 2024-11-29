from django.urls import path
from api import views

urlpatterns = [
    path('', views.Generator.as_view()),
]