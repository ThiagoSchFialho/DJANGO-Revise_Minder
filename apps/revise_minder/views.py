from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import date, timedelta

from apps.revise_minder.forms import SubjectForm, StudyForm
from apps.revise_minder.models import Subject, Study, Revision

def calc_revisions(study):
    plus_1_day = study.date + timedelta(days=1)
    plus_1_week = study.date + timedelta(weeks=1)
    plus_1_month = study.date + timedelta(days=30)

    revision = Revision(study=study, date=plus_1_day)
    revision.save()

    if study.revisions_cycles >= 2:
        revision = Revision(study=study, date=plus_1_week)
        revision.save()

    if study.revisions_cycles == 3:
        revision = Revision(study=study, date=plus_1_month)
        revision.save()

def index(request):
    return render(request, 'revise_minder/index.html')

def revisions_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    date_today = date.today()

    today_revisions = Revision.objects.filter(date=date_today)
    done_revisions = today_revisions.filter(is_done=True)
    today_revisions = today_revisions.filter(is_done=False)
    next_revisions = Revision.objects.filter(date__gt=date_today)
    
    return render(request, 'revise_minder/revisions_home.html', {'today_revisions':today_revisions, 'next_revisions':next_revisions, 'done_revisions':done_revisions})

def revision_done(request, revision_id):
    revision = Revision.objects.get(id=revision_id)

    if revision.is_done:
        revision.is_done = False
    else:
        revision.is_done = True

    revision.save()
    return redirect(revisions_home)

def past_revisions(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    past_revisions = Revision.objects.filter(date__lt=date.today())

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
            study.save()
            calc_revisions(study)

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
            study = form.save(commit=False)
            revisions = Revision.objects.filter(study=study)

            for revision in revisions:
                revision.delete()

            study.save()
            calc_revisions(study)

            return redirect('my_studies')

    return render(request, 'revise_minder/edit_study.html', {'form':form, 'study_id':study_id})

def delete_study(request, study_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    study = Study.objects.get(id=study_id)
    study.delete()
    return redirect('my_studies')