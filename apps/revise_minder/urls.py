from django.urls import path
from apps.revise_minder.views import index, revisions_home, subject, add_study, my_studies

urlpatterns = [
    path('', index, name='index'),
    path('revisions/', revisions_home, name='revisions_home'),
    path('subject/', subject, name="subject" ),
    path('add_study/', add_study, name='add_study'),
    path('my_studies/', my_studies, name='my_studies')
]
