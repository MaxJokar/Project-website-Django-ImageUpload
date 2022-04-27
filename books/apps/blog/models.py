# from distutils.command.upload import upload
# from tabnanny import verbose
# from turtle import title
from django.db import models
# from django.utils import timezone


class Blog(models.Model):
    title=models.CharField(max_length=200,verbose_name='Title of our Article')
    description=models.TextField(verbose_name='Text of our Article')
    is_active=models.BooleanField(default=False,verbose_name='active/unactive')
    main_img=models.ImageField(upload_to='images/blogimg',verbose_name='Final picture')
    #if in our model we dont use FileField we should  check in view like:if imageUploat is jpg or png ..


    def __str__(self) :
        return self.title+"\n"+ self.description+"\n"+self.is_active







# class Author(models.Model):
#     # id=models.IntegerField(primary_key=True)
#     name=models.CharField(max_length=30)
#     family=models.CharField(max_length=30)
#     slug=models.SlugField(max_length=100)
#     age=models.IntegerField(default=20)
#     is_active=models.BooleanField(default=True)
#     register_date=models.DateTimeField(default=timezone.now)
#     email=models.EmailField(max_length=100)
#     image_name=models.CharField(max_length=200,default='nophoto',null=True,blank='True')
    
    
#     def __str__(self) :
#         return f"{self.name}\t{self.family}\t{self.age}"