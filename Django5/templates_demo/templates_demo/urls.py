"""
URL configuration for templates_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('baidu/', views.baidu, name='baidu'),
    path('info', views.info, name="info"),
    path('if',views.if_view,name="if"),
    path('for',views.for_view,name="for"),
    path('with',views.with_view,name="with"),
    path('url',views.url_view,name="url"),
    path('template/form',views.template_view,name="template_form"),
]
