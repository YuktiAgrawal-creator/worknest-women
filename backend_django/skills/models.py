from django.db import models

class Skill(models.Model):
    DEMAND_CHOICES = (
        ('Low','Low'),('Medium','Medium'),('High','High')
    )
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)
    icon = models.CharField(max_length=64, default='🌟')
    description = models.TextField(blank=True, null=True)
    demandLevel = models.CharField(max_length=10, choices=DEMAND_CHOICES, default='Medium')
    avgPay = models.FloatField(default=0)

    def __str__(self):
        return self.name
