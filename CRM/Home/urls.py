from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.show_home, name='main'),
    path('login/', views.login_page, name='login'),
    path('create_user/', views.create_user, name='create_user')
]