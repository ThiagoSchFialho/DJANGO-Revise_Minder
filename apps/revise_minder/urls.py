from django.urls import path
from apps.revise_minder.views import index, revisions_home

urlpatterns = [
    path('', index, name='index'),
    path('revisions/', revisions_home, name='revisions_home')
]
