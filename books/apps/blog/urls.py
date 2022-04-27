# from django.urls import path
# import apps.blog.views as views
from django.urls import path
from .views import create_blog,index

            
urlpatterns = [
     path('',index,name="blog_index"),
     path('add/',create_blog,name="create_blog"),

     
     # path('view0/',fun0),
     # path('view1/',ViewClass1.as_view(),name="ViewClass1"),
     
     
     # path('',views.index),
     # path('authors',views.showAuthors),
     # path('author/<int:author_id>',views.authorDetail),
     
    
    
]           