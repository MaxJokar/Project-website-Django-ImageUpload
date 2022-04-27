from django import template
from django.conf import settings
from django.urls import path
import apps.mainapp.views as views
#5.AS SOON AS WE IMPORT SETTING , ]+STATIC(.......)  WE SHOULD IMPORT IN HEADER THE 
from django.conf.urls import static


urlpatterns=[
      # path('',views.index),
      # path('step1/',views.step1),
      # path('step2/',views.step2),
      # path('names/',views.names),
      # path('table/',views.table),
      # path('step10/',views.step10,name="template10"),
      # path('test1/',views.test1,name="template1"),
      # path('test2/',views.test2,name="template2"),
      # path('page11/',views.page11,name="template11"),
      # path('page12/',views.page12,name="template12"),
               
]
    
  
  # template2 is  the name url of that action which is  step10 here           
            