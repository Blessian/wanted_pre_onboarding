from django.db import models


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)


class Recruit(models.Model):
    company = models.IntegerField()
    company_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    recruit_position = models.CharField(max_length=100)
    reward = models.PositiveIntegerField()
    content = models.TextField()
    skills = models.CharField(max_length=100)


class Applicant(models.Model):
    applicant_name = models.CharField(max_length=100, unique=True)
    recruit = models.IntegerField(null=True, blank=True)
