from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30,blank=True, null=True,)
    reg        = models.IntegerField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'N/A'),
    )
    gender     = models.CharField(max_length=1, choices=GENDER)
    dob        = models.DateField()
    photo      = models.CharField(max_length=210,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Result(models.Model):
    student_id = models.IntegerField()
    class_name = models.CharField(max_length=100,blank=False, null=False,)
    year       = models.IntegerField()    
    total_marks= models.IntegerField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)	
		