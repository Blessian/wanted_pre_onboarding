from django.urls import path

from . import views

app_name = 'wanted'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recruit_id>/', views.detail, name='detail'),
    path('recruit/create/', views.create, name='recruit_create'),
    path('recruit/modify/<int:recruit_id>', views.modify, name='recruit_modify'),
    path('recruit/delete/<int:recruit_id>', views.delete, name='recruit_delete'),
]
