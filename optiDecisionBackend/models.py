# models.py
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)


class Criteria(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class SubCriteria(models.Model):
    name = models.CharField(max_length=100)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE)
