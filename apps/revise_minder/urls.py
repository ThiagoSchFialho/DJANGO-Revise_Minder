from django.urls import path
from apps.revise_minder.views import index, reviews_home

urlpatterns = [
    path('', index, name='index'),
    path('reviews/', reviews_home, name='reviews_home')
]
