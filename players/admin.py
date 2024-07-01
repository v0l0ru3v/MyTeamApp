
from django.contrib import admin
from .models import Player, Team  # Импортируйте вашу модель Player

# Зарегистрируйте модель Player
admin.site.register(Player)

admin.site.register(Team)
