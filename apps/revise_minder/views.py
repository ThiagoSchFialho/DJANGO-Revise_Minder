from django.shortcuts import render

def index(request):
    return render(request, 'revise_minder/index.html')

def revisions_home(request):
    return render(request, 'revise_minder/revisions_home.html')