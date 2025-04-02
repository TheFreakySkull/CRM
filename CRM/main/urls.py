from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.crm, name='crm'),
    path('do_task/<int:id>', views.do_task, name='do_task'),
    path('create_task/', views.create_task, name='create_task'),
    path('change_task/<int:id>', views.change_task, name='change_task'),
    path('del_task/<int:id>', views.del_task, name='del_task')
]
