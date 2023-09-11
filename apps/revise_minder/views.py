from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import date

from apps.revise_minder.forms import SubjectForm, StudyForm
from apps.revise_minder.models import Subject, Study, Revision

class Revision_info:
    def __init__(self, revision, date):
        self.revision = revision
        self.date = date

def index(request):
    return render(request, 'revise_minder/index.html')

def revisions_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    today_date = date.today()

    revisions_today = Revision.objects.filter(
        Q(date_plus_1_day=today_date) | Q(date_plus_1_week=today_date) | Q(date_plus_1_month=today_date)
    )

    revisions = Revision.objects.all()
    next_revisions = []

    for revision in revisions:
        if revision.study.revisions_cycles >= 1:
            if revision.date_plus_1_day > date.today():
                revision_info = Revision_info(revision, revision.date_plus_1_day)
                next_revisions.append(revision_info)
        
        if revision.study.revisions_cycles >= 2:
            if revision.date_plus_1_week > date.today():
                revision_info = Revision_info(revision, revision.date_plus_1_week)
                next_revisions.append(revision_info)

        if revision.study.revisions_cycles == 3:
            if revision.date_plus_1_month > date.today():
                revision_info = Revision_info(revision, revision.date_plus_1_month)
                next_revisions.append(revision_info)

    next_revisions.sort(key=lambda x:x.date)
    
    return render(request, 'revise_minder/revisions_home.html', {'revisions_today':revisions_today, 'next_revisions':next_revisions})

def past_revisions(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    revisions = Revision.objects.all()
    past_revisions = []

    for revision in revisions:
        if revision.study.revisions_cycles >= 1:
            if revision.date_plus_1_day < date.today():
                revision_info = Revision_info(revision, revision.date_plus_1_day)
                past_revisions.append(revision_info)
        
        if revision.study.revisions_cycles >= 2:
            if revision.date_plus_1_week < date.today():
                revision_info = Revision_info(revision, revision.date_plus_1_week)
                past_revisions.append(revision_info)

        if revision.study.revisions_cycles == 3:
            if revision.date_plus_1_month < date.today():
                revision_info = Revision_info(revision, revision.date_plus_1_month)
                past_revisions.append(revision_info)

    past_revisions.sort(key=lambda x:x.date)

    return render(request, 'revise_minder/past_revisions.html', {'past_revisions':past_revisions})

def subject(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = SubjectForm()
    subjects = Subject.objects.filter(user=request.user)

    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect('subject')

    return render(request, "revise_minder/subject.html", {'form':form, 'subjects':subjects})

def edit_subject(request, subject_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    subject = Subject.objects.get(id=subject_id)
    form = SubjectForm(instance=subject)

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)

        if form.is_valid():
            form.save()
            return redirect('subject')

    return render(request, 'revise_minder/edit_subject.html', {'form':form, 'subject_id':subject_id})

def delete_subject(request, subject_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    return redirect('subject')

def add_study(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = StudyForm(user=request.user)
    
    if request.method == 'POST':
        form = StudyForm(request.POST, user=request.user)

        if form.is_valid():
            study = form.save(commit=False)
            study.user = request.user

            revision = Revision(study=study, date=study.date)

            study.save()
            revision.save()

            return redirect('my_studies')
        
    return render(request, 'revise_minder/add_study.html', {'form':form})

def my_studies(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    studies = Study.objects.filter(user=request.user)
    return render(request, 'revise_minder/my_studies.html', {'studies':studies})

def edit_study(request, study_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    study = Study.objects.get(id=study_id)
    form = StudyForm(instance=study, user=request.user)

    if request.method == "POST":
        form = StudyForm(request.POST, instance=study, user=request.user)

        if form.is_valid():
            revision = Revision.objects.get(study=study)
            revision.date = study.date

            form.save()
            revision.save()

            return redirect('my_studies')

    return render(request, 'revise_minder/edit_study.html', {'form':form, 'study_id':study_id})

def delete_study(request, study_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    study = Study.objects.get(id=study_id)
    study.delete()
    return redirect('my_studies')