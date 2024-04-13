from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def baidu(request):
    return render(request, 'baidu.html')

def info(request):
    # 1.普通变量
    username = 'Pigasso'
    # 2.字典类型
    book ={'name': "123", 'auther': "654", 'title': "789"}
    # 3.列表
    books = [
        {'name': "123", 'auther': "456", 'title': "789"},
        {'name': "321", 'auther': "654", 'title': "987"},
    ]
    #4.对象
    class person:
        def __init__(self, name):
            self.name = name

    context = {
        'username': username,
        'book': book,
        'books' : books,
        'person': person('Pigasso')
    }

    return render(request, 'info.html', context)

def if_view(request):
    age = 18
    return render(request, 'if.html', context={'age':age})


def for_view(request):
    # 1.列表
    books = [
        {'name': "123", 'auther': "456", 'title': "789"},
        {'name': "321", 'auther': "654", 'title': "987"},
    ]
    # 在模版中，不能使用break和continue
    context = {
        'books': books,
    }
    return render(request, 'for.html', context)

def with_view(request):
    context = {
        'books':[
            {'name': "123", 'auther': "456", 'title': "789"},
            {'name': "321", 'auther': "654", 'title': "987"},
        ]
    }
    return render(request, 'with.html', context)

def url_view(request):
    return render(request, 'url.html')

def template_view(request):
    return render(request, 'xfz_index.html')