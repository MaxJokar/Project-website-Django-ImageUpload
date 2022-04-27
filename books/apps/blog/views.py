
from multiprocessing import context
from tkinter import image_types
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.core.files.storage import FileSystemStorage
import os 
import datetime
from django.conf import settings


# from multiprocessing import context
# from django.views import View

# def fun0(request):
#     context={ 
#         'name':'Max Jokar'
#     }
#     return render(request,'viewtest/page1.html',context)



# class ViewClass1(View):
#     def get(self,request):
#         context={
            
#             'name':'Max Jokar'
#         }
        
#         return render(request,'viewtest/page1.html',context)     



def index(request):
    blogs=Blog.objects.all()
    context={
        "blogs":blogs,
        "media_url":settings.MEDIA_URL,
        }
    return render(request,"blog/index.html",context)


def create_blog(request):
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES) #is a dictionary of files coming++=request to give us files too (we recive datafile too)  
        if form.is_valid():
            iamgeUpload=request.FILES['main_img'] # main_img is the name of our file (we get fotos)
            if   iamgeUpload.size<10000 :
                if  iamgeUpload.content_type=="image/jpeg" or iamgeUpload.content_type=="image/png" : #type of  given file 
                    imgName,ext=os.path.splitext(iamgeUpload.name)     # split the name and prefix ,the real name in imaName and prefix is saved in ext 
                    currenttime=datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f") #we get moment info about fotos 
                    
                    # imagePath='images/blogimg'+iamgeUpload.name       #to save in our data  
                    # imagePath='images/blogimg'+imgName+currenttime+ext
                    imagePath='images/blogimg'+imgName+currenttime+ext
                    
                    #Below dedicated to storage  in our dataBase:
                    data=form.cleaned_data  #save in dataBase  from here starts:
                    blog=Blog()
                    blog.title=data['title']
                    blog.description=data['description']
                    blog.is_active=data['is_active']
                    blog.main_img=imagePath              #To save as one of our field blog=save in database
                    blog.save()
                    #Below is dedicated to storage  our file
                    fss=FileSystemStorage()    #These part  is save of file  on the server
                    fss.save(imagePath,iamgeUpload) # (address'name address and place of save ', imageupload=the file wants to save )
                    return redirect(request,"blog/index.html")
                else:
                        context={
                                'form':form, #those context come from form should have  the main  form 
                                'message':'the type of file is not correct: jpg or png Only'
                        }
        else:
            context={
                    'form':form, #those context come from form should have  the main  form 
                    'message':'the size must not More than 10 kilo Byte'
                }
    else:
        form=BlogForm()
        context={
            'form':form,
        }
        
        return render(request,"blog/create.html",context)































# from django.shortcuts import render
# from django.http import HttpResponse,Http404
# from django.conf import settings
# # from apps.blog.models import Author
# from .models import Author


# def index1(request):
#     blogList=[
#         {
#             'imagename':'th.jfif',
#             'blogTitle':'English teacher',
#             'summeryDesctiption':'the students nowadays are more impatient and to grab their attention, teaching methods need to cater to their dynamic thinking process',
#             'registerDate':'05.01.2018'
         
         
#          },
        
#         {
#             'imagename':'th1.jfif',
#             'blogTitle':'Russian Teacher',
#             'summeryDesctiption':'У преподавания языков есть свои проблемы. В большинстве случаев это иностранный язык, который учащийся не может понять из своего окружения,,',
#             'registerDate':'05.11.2015'
         
         
#          },
#         {
#             'imagename':'th4.jfif',
#             'blogTitle':'French Teacher',
#             'summeryDesctiption':'leur base de connaissances senrichit des informations disponibles sur Internet',
#             'registerDate':'12.01.2022'
         
         
#          },
#         {
#             'imagename':'th5.jfif',
#             'blogTitle':'Italian Teacher',
#             'summeryDesctiption':'la generazione attuale ottiene visibilità nel mondo attraverso i social media',
#             'registerDate':'05.01.2018'
         
         
#          },
        
        
    # ]
    
# def index(request):
#     authors=Author.objects.all() # load all  datas in our table 
#     context={
#             'media_url':settings.MEDIA_URL,
#             "imagename":'th1.jfif',
#             'authors':authors
#             # 'blogList':blogList,
            
        
#         }

#     return render(request,'blog/index.html',context)

    
    
    
# def showAuthors(request):
#     authors=Author.objects.all() # load all  datas in our table 
#     context={
#             'media_url':settings.MEDIA_URL,
#             # "imagename":'th1.jfif',
#             'authors':authors
#             # 'blogList':blogList,
            
        
#         }
 
#     return render(request,'blog/authors.html',context)


# To have additional information about the  Tutor we can  use  Description section which one href  opens it . 

# def authorDetail(request,author_id):
#     try:
        
#         author=Author.objects.get(id=author_id)
#     except Author.DoesNotExist:  
#             raise Http404("This Page Does not Exit TTTTT")  
#     context={
#                 'media_url':settings.MEDIA_URL,
            
#                 'author':author
            

            
#             }
        
#     return render(request, 'blog/author_detail.html',context)








 