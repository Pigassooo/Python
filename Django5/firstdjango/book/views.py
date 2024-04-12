from django.shortcuts import render,HttpResponse


def book_detail_query_string(request):
    book_id = request.GET.get('id')
    book_name = request.GET.get('name')
    return HttpResponse(f"您查找的图书id是：{book_id}  name:{book_name}" )