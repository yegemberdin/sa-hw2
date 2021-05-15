from django.urls import path
from .views import list_users, create_user, update_user, delete_user

urlpatterns = [
    path('', list_users, name="list_users"),
    path('new', create_user, name='create_users'),
    path('update/<int:id>', update_user, name='update_user'),
    path('delete/<int:id>', delete_user, name='delete_user')
]

