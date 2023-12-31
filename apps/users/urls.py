from django.urls import path
from apps.users.views import login, signup, logout, my_account, delete_account, update_password

urlpatterns = [
    path('login/', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout/', logout, name="logout"),
    path('my_account', my_account, name='my_account'),
    path('delete_account', delete_account, name='delete_account'),
    path('update_password', update_password, name='update_password')
]
