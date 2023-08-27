from django.shortcuts import render

def index(request):
    return render(request, 'revise_minder/index.html')

def reviews_home(request):
    return render(request, 'revise_minder/reviews_home.html')