from django.db import models

# Create your models here.
class Student(models.Model):   
    Name= models.CharField(max_length=50)
    Email= models.EmailField()
    Contact= models.IntegerField()
    Add= models.CharField(max_length=100)
    Age=  models.IntegerField(max_length=100,null=True)

    class Meta:
        ordering=["Name"]
        verbose_name="stu"
