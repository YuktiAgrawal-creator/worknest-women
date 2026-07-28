from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_transactions),
    path('create', views.create_transaction),
]
