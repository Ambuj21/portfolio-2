from django.db import models


class ProjectDetail (models.Model):
    pro_id = models.IntegerField(primary_key=True)
    pro_img = models.FileField(upload_to='project_imgs/')
    pro_name = models.CharField(max_length=50)
    pro_description = models.TextField(max_length= 100)
    project_link = models.URLField(default='/')


class UserDetail (models.Model):
    user_img = models.FileField(upload_to='user_imgs')
    about = models.TextField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    skills = models.TextField(max_length=150, default="None")


class Certificates (models.Model):
    cert_img = models.FileField(upload_to='certificates')
    crt_name = models.CharField(max_length=100)
    crt_description = models.TextField(max_length=100, default='None')
    Link = models.URLField(default="/")
