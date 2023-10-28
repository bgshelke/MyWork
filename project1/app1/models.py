from django.db import models

# Create your models here.
class Enquiry(models.Model):
    sno=models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=80)
    mobile = models.BigIntegerField()
    education = models.CharField(max_length=80)
    stream =models.CharField(max_length=80,null=True)
    college = models.CharField(max_length=80,null=True)
    gender = models.CharField(max_length=20)
    pass_year = models.IntegerField()
    course = models.CharField(max_length=80)
    b_type = models.CharField(max_length=80)
    reff = models.CharField(max_length=200)
    remark = models.CharField(max_length=255)

