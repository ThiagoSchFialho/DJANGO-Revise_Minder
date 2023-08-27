from django.urls import path
from apps.users.views import login

urlpatterns = [
    path('login/', login, name='login'),
]
