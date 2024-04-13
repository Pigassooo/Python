from django.shortcuts import render, HttpResponse

# Create your views here.


def movie_list(request):
    return HttpResponse("movie list")

def movie_detail(request, movie_id):
    return HttpResponse(f"movie id :{movie_id}")

