from django.shortcuts import render, redirect
from apps.revise_minder.forms import SubjectForm

def index(request):
    return render(request, 'revise_minder/index.html')

def revisions_home(request):
    return render(request, 'revise_minder/revisions_home.html')

def subject(request):
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('subject')

    return render(request, "revise_minder/subject.html", {'form':form})