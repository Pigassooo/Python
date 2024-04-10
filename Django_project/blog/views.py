from django.shortcuts import render

posts=[
    {
        'author': 'Pigasso',
        'title':'Blog Post 1',
        'content':'This is the first post',
        'date_posted':'April 9, 2024',
    },
    {
        'author': 'Ivy',
        'title':'Blog Post 2',
        'content':'This is the second post',
        'date_posted':'April 10, 2024',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})