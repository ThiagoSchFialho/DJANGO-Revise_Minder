from django.urls import path
from apps.revise_minder.views import index, revisions_home, past_revisions, revision_done, subject, delete_subject, edit_subject, add_study, my_studies, delete_study, edit_study

urlpatterns = [
    path('', index, name='index'),
    path('revisions/', revisions_home, name='revisions_home'),
    path('past_revisions/', past_revisions, name='past_revisions'),
    path('revision_done/<int:revision_id>', revision_done, name='revision_done'),
    path('subject/', subject, name="subject" ),
    path('delete_subject/<int:subject_id>', delete_subject, name='delete_subject'),
    path('edit_subject/<int:subject_id>', edit_subject, name='edit_subject'),
    path('add_study/', add_study, name='add_study'),
    path('my_studies/', my_studies, name='my_studies'),
    path('delete_study/<int:study_id>', delete_study, name='delete_study'),
    path('edit_study/<int:study_id>', edit_study, name='edit_study')
]
