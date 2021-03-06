from django.contrib import admin
from .models import Contact,Skill,Image,About,Education,Social,Welcome,MyProject,Document
# Register your models here.

@admin.register(Contact)
class Contact_admin(admin.ModelAdmin):
    list_display=['name','email','message']

@admin.register(Skill)
class Skill_admin(admin.ModelAdmin):
    list_display=['name','number']


@admin.register(Image)
class Image_admin(admin.ModelAdmin):
    list_display=['img']


@admin.register(About)
class About_admin(admin.ModelAdmin):
    list_display=['about']


@admin.register(Education)
class Education_admin(admin.ModelAdmin):
    list_display=['title','subtitle','image']


@admin.register(Social)
class Social_admin(admin.ModelAdmin):
    list_display=['name','img']

@admin.register(Welcome)
class Welcome_admin(admin.ModelAdmin):
    list_display=['name','line1','line2']

@admin.register(MyProject)
class Project_admin(admin.ModelAdmin):
    list_display=['title','about','img','lang']


@admin.register(Document)
class Document_admin(admin.ModelAdmin):
    list_display=['resume']