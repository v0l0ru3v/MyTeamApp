# players/views.py

from django.shortcuts import render
from .models import Team, Player

def teams_list(request):
    teams = Team.objects.all()
    return render(request, 'players/teams_list.html', {'teams': teams})

def team_players(request, year):
    team_players = Player.objects.filter(birth_year=year)
    return render(request, 'players/team_players.html', {'team_players': team_players, 'year': year})
