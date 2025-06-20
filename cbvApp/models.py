from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_price = models.IntegerField()
    course_description = models.TextField()
    course_instructor = models.CharField(max_length=100)
    course_rating = models.IntegerField()