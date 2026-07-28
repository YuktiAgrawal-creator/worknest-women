from django.db import models
from django.conf import settings

class Job(models.Model):
    TYPE_CHOICES = (
        ('remote','remote'),('onsite','onsite'),('hybrid','hybrid'),('freelance','freelance')
    )
    STATUS_CHOICES = (
        ('open','open'),('closed','closed'),('filled','filled')
    )
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.JSONField(default=list, blank=True)
    skills = models.ManyToManyField('skills.Skill', blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='remote')
    category = models.CharField(max_length=255)
    salary = models.JSONField(default=dict, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    postedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posted_jobs', on_delete=models.SET_NULL, null=True)
    applicants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='applied_jobs', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    isWomenOnly = models.BooleanField(default=True)
    tags = models.JSONField(default=list, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
