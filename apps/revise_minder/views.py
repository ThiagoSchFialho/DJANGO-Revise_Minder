from django.shortcuts import render, redirect
from apps.revise_minder.forms import SubjectForm, StudyForm
from apps.revise_minder.models import Subject, Study

def index(request):
    return render(request, 'revise_minder/index.html')

def revisions_home(request):
    return render(request, 'revise_minder/revisions_home.html')

def subject(request):
    form = SubjectForm()

    subjects = Subject.objects.all()

    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('subject')

    return render(request, "revise_minder/subject.html", {'form':form, 'subjects':subjects})

def add_study(request):
    form = StudyForm()
    
    if request.method == 'POST':
        form = StudyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('my_studies')
        
    return render(request, 'revise_minder/add_study.html', {'form':form})

def my_studies(request):
    studies = Study.objects.all()
    return render(request, 'revise_minder/my_studies.html', {'studies':studies})