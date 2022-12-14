"""HardikP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from app1.forms import Item_form
from app1.views import contact, display_images, success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('image_upload',contact,name='image_upload'),
    # path('accounts',include('accounts.urls')),
    # path('',include('django.contrib.auth.urls')),
    
    
    
    path('item_images',display_images,name='item_images'),
    
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)