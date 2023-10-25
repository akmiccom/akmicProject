from django.db import models

class Calculator(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title