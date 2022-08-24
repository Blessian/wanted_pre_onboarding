from django.urls import path

from . import views

app_name = 'wanted'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recruit_id>/', views.detail, name='detail'),
    path('recruit/create/', views.create, name='recruit_create')
]
