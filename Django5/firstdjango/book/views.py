from django.shortcuts import render,HttpResponse


app_name = 'book'

def book_detail_query_string(request):
    book_id = request.GET.get('id')
    book_name = request.GET.get('name')
    return HttpResponse(f"您查找的图书id是：{book_id}  name:{book_name}" )

def book_detail_path(requests, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}" )

def book_str(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")

def book_slug(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")

def book_path(request, book_id):
    return HttpResponse(f"您查找的图书id是：{book_id}")