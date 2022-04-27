from django.contrib import admin
from django.urls import path,include
from django.conf import settings #to use  setting in +static we should add this part
from django.conf.urls.static import static #aslo required after +setting To be recognized  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.mainapp.urls')),
    path('blog/',include('apps.blog.urls')),
    path('post/',include('apps.blog.urls'),name=""),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_header='Manager of the website '
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# this static added after  media_url in step10 is used in html as finalwith ((media_url))