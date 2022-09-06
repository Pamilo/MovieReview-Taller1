from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request,'home.html')
    #return render(request,'home.html',{'name':'Pablo Micolta Lopez'})
    searchTerm= request.GET.get('searchMovie')
    if searchTerm:
        movies=Movie.objects.filter(Title__icontains=searchTerm)
    else:
        movies=Movie.objects.all()

    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')



# Create your views here.
