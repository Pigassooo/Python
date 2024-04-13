"""
URL configuration for firstdjango project.

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
from django.http import HttpResponse
from django.urls import path, include
from book import views
from django.urls import reverse

def index(request):
    # # print(reverse('index'))
    # print(reverse('book_str', kwargs={'book_id': 1}))

    # 如果查询字符串的方式传参，那么只能通过字符串拼接的方式来实现
    # print(reverse('book_detail_query_string') + '?id=1')

    # 指定命名空间
    # print(reverse('movie:movie_list'))
    return HttpResponse("<h1>Welcome to Blog Home</h1>")

urlpatterns = [
    # path(route, view, name=None, kwargs=None)
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    # http://127.0.0.1:8000/book?id=1
    path('book/',views.book_detail_query_string),

    # http://127.0.0.1:8000/book/1
    # 在book_id前指定参数类型有两点好处
    # 1. 以后在浏览器中如果输入的是非整形，会出现404错误
    # 2. 在view视图函数中得到的id就是整形
    path('book/<int:book_id>',views.book_detail_path),
    path('book/str/<str:book_id>',views.book_str, name='book_str'),
    path('book/slung/<slug:book_id>',views.book_slug, name="book_slug"),
    path('book/path/<path:book_id>',views.book_path, name='book_path'),

    path('movie/',include('movie.urls'))
]
