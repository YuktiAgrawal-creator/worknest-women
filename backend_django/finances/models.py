from django.db import models
from django.conf import settings

class Transaction(models.Model):
    TYPE_CHOICES = (('income','income'),('expense','expense'))
    STATUS_CHOICES = (('pending','pending'),('completed','completed'),('failed','failed'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.FloatField()
    category = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    job = models.ForeignKey('jobs.Job', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')

    def __str__(self):
        return f"{self.type} {self.amount}"
