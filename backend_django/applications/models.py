from django.db import models
from django.conf import settings

class Application(models.Model):
    STATUS_CHOICES = (
        ('pending','pending'),('reviewed','reviewed'),('interview','interview'),('accepted','accepted'),('rejected','rejected')
    )
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    coverLetter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    interviewDate = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    appliedAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Application {self.id} for job {self.job_id}"
