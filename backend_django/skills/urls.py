from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_skills),
    path('create', views.create_skill),
]
