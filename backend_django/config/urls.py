from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/users/', include('accounts.urls_users')),
    path('api/jobs/', include('jobs.urls')),
    path('api/applications/', include('applications.urls')),
    path('api/skills/', include('skills.urls')),
    path('api/transactions/', include('finances.urls')),
    path('api/health', lambda request: __import__('django.http').HttpResponse(
        __import__('json').dumps({"status":"OK","message":"WorkNest API running","env":__import__('os').environ.get('DJANGO_SETTINGS_MODULE','')},), content_type='application/json')),
]
