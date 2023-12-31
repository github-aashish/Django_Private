from django.db import models

# Create your models here.


class info_customer(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(null=True)
    phone_no = models.IntegerField(null=True)
    message=models.TextField(null=True)
