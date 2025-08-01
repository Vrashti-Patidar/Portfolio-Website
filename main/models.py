from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    message=models.TextField(max_length=350)
    # def __str__(self):
    #     return self.name 