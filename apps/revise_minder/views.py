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

def edit_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    form = SubjectForm(instance=subject)

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)

        if form.is_valid():
            form.save()
            return redirect('subject')

    return render(request, 'revise_minder/edit_subject.html', {'form':form, 'subject_id':subject_id})

def delete_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    return redirect('subject')

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

def edit_study(request, study_id):
    study = Study.objects.get(id=study_id)
    form = StudyForm(instance=study)

    if request.method == "POST":
        form = StudyForm(request.POST, instance=study)

        if form.is_valid():
            form.save()
            return redirect('my_studies')

    return render(request, 'revise_minder/edit_study.html', {'form':form, 'study_id':study_id})

def delete_study(request, study_id):
    study = Study.objects.get(id=study_id)
    study.delete()
    return redirect('my_studies')