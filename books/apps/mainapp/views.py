from django.shortcuts import render
from django.http import  HttpResponse
from django.template import context
from django.conf import settings #3 new one after we tested the final2 
# from django.template import loader
#========================================================================================================
def index(request):
    return HttpResponse('Main  Home apage ........apps.mainapp.view.index')

# def step1(request):
#     template=loader.get_template('mainapp/mainPageSite.html')
#     return HttpResponse(template.render())
#========================================================================================================
def step1(request):
    return render(request,'mainapp/mainPageSite.html')

# def step2(request):
#     return render(request,'mainapp/secondPageSite.html')
#========================================================================================================
import datetime
def step2(request):
    today=datetime.datetime.now
    context={
        "name":"Max",
        "age":"35",
        "n":"100",
        "today":today,
        "names":['Jack','Natasha','Max','Shandiz ']
        
    }
    return render(request,'mainapp/secondPageSite.html',context)
#========================================================================================================
import datetime
def names(request):
    today=datetime.datetime.now
    # variable are taken from the view towards the  templates and displayed ,context convery all dataS , we have a counter with one For 
    context={
        "name":"Max",
        "age":"35",
        "n":"100",
        "today":today,
        "names":['Jack','Natasha','Max'],
        "range":range(1,11)   # we check the range and FOR.
        
    }
    return render(request,'mainapp/names.html',context)
#========================================================================================================

# import datetime
def table(request):
    # today=datetime.datetime.now
    context={
        "row":range(5),
        "col":range(5),
    }
    return render(request,'mainapp/table.html',context)

#========================================================================================================
import os  # After you had decided to send a  list of picS this should be imported 
def step10(request):
    imageList=os.listdir(settings.MEDIA_ROOT+'/images') # (sends a list of  picS).==>MEDIA_ROOT=os.path.join(BASE_DIR,'media/')
    context={
        'media_url':settings.MEDIA_URL,
        # "imageName":'th.jfif' #New added in Python and send to HTML 
        "imageList":imageList
    }
    
    return render(request,'mainapp/final.html',context)

#========================================================================================================
   # 'media_url':settings.MEDIA_URL    #3 : is very important and not '='


# def testMeidaUrl(request):
#     context={
#         'media_url':settings.MEDIA_URL 
        
#     }
    
#     return render(request,'mainapp/testMeidaUrl.html',context)
#===========================================================================================

def test1(request):
    imageList=os.listdir(settings.MEDIA_ROOT+'/images')
    context={
        'media_url':settings.MEDIA_URL,   
          "imageList":imageList, 
    
    
    }
 
    return render(request,'mainapp/test1.html',context)
# without using  CSS  and  just  one  Lenear for  pics

#===========================================================================================

def test2(request):
    imageList=os.listdir(settings.MEDIA_ROOT+'/images')
    context={
        'media_url':settings.MEDIA_URL,   
          "imageList":imageList, 
    
    
    }
 
    return render(request,'mainapp/test2.html',context)
#===========================================================================================



def page11(request):
    return render(request,'mainapp/page11.html')

#=========================================================================

def page12(request):
    
    context={
        'media_url':settings.MEDIA_URL,
        "imageName":'th.jfif',
      
    }

    return render(request,'mainapp/page12.html',context)


#====================================================================
def index(request):
    
    context={
        'media_url':settings.MEDIA_URL,
        "imageName":'th.jfif',
      
    }

    return render(request,'mainapp/page12.html',context)











