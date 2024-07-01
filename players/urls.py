from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_list, name='teams_list'),
    path('<int:year>/', views.team_players, name='team_players'),
]
