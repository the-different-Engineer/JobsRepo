from django.db import models

# Create your models here.

class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibiity = models.CharField(max_length=100)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibiity = models.CharField(max_length=100)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class BangloreJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibiity = models.CharField(max_length=100)
    address = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
