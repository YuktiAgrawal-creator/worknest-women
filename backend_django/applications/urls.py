from django.urls import path
from . import views

urlpatterns = [
    path('', views.apply_job),
    path('my', views.get_my_applications),
]
