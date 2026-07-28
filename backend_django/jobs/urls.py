from django.urls import path
from . import views

urlpatterns = [
    # Single route handles GET (list) and POST (create)
    path('', views.jobs_list_create, name='jobs-list-create'),
    path('recommended', views.get_recommended, name='jobs-recommended'),
    path('my', views.get_my_jobs, name='jobs-my'),
    path('<int:id>', views.get_job, name='jobs-detail'),
    path('<int:id>/update', views.update_job, name='jobs-update'),
]
