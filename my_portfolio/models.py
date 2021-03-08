from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    message=models.TextField()


class Skill(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()

class About (models.Model):
    about= models.TextField()


class Image(models.Model):
    img=models.ImageField( upload_to='images/')


class Education(models.Model):
    title=models.CharField( max_length=50)
    subtitle=models.CharField( max_length=100)
    image=models.ImageField( upload_to='images/')

class Social(models.Model):
    name=models.CharField( max_length=50)
    img=models.ImageField( upload_to='images/')
    link=models.URLField( max_length=200,default=None,null=True,blank=True)

class Welcome(models.Model):
    name=models.CharField(max_length=50)
    line1=models.CharField( max_length=50)
    line2=models.CharField( max_length=50)

class MyProject(models.Model):
    title=models.CharField( max_length=50)
    about=models.CharField( max_length=100)
    lang=models.CharField(max_length=50,default=None,null=True,blank=True)
    img=models.ImageField( upload_to='images/')
    repo=models.URLField( max_length=200,default=None,null=True,blank=True)
    link=models.URLField( max_length=200,default=None,null=True,blank=True)


class Document(models.Model):
    resume=models.FileField( upload_to='documents/', max_length=500)