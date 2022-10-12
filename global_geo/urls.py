"""global_geo URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from globalgeo.views import home_view,about_view, detailbooks_view,detailpost_view,categpost

urlpatterns = [
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home_url'),
    path('categpost/<str:cats>/', categpost, name='categpost_url'),
    path('about/', about_view, name='about_url'),
    path('detaillbooks/<str:cats>/', detailbooks_view, name='detailbooks_url'),
    path('detaillpost/<int:pk>/', detailpost_view, name='detailpost_url'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)