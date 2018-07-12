from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=80)
    school_address = models.CharField(max_length=200)
    school_contact = models.CharField(max_length=40)
    school_phone = models.BigIntegerField()
    pub_date = models.DateTimeField('date published')


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=80)
    teacher_address = models.CharField(max_length=200)
    teacher_email = models.CharField(max_length=40)
    teacher_phone = models.CharField(max_length=40)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class DCAM(models.Model):
    dcam_name = models.CharField(max_length=80)
    dcam_office = models.CharField(max_length=200)
    dcam_email = models.CharField(max_length=200)
    dcam_phone = models.CharField(max_length=40)


    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)