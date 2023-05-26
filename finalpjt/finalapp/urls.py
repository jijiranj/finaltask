from django.contrib import admin
from django.urls import path
from .import views
app_name='finalapp'

urlpatterns = [path('',views.demo,name='demo'),
               path('branch/<int:branch_id>/', views.detail, name='detail'),
               path('login',views.login,name='login'),
               path('register',views.register,name='register'),
               path('user_registration',views.user_registration,name='user_registration'),
               path('logout', views.logout, name='logout'),
               path('new', views.new, name='new'),
               ]