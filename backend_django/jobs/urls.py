from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_jobs),
    path('recommended', views.get_recommended),
    path('my', views.get_my_jobs),
    path('<int:id>', views.get_job),
    path('', views.create_job),
    path('<int:id>', views.update_job),
]
