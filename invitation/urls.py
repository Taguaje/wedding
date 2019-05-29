from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('confirm_invite/', views.confirm_invite, name='confirm_invite')
]
