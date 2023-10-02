from django.db import models

# Create your models here.
class User(models.Model):
    student_name = models.TextField()
    erp = models.TextField()
    plate_num = models.TextField()
    program = models.TextField()


class record(models.Model):
    plate_num = models.TextField()
    entered_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(auto_now=True)