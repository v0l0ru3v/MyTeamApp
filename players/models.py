from django.db import models

class Team(models.Model):
    year = models.IntegerField(unique=True)  # Год команды должен быть уникальным

    def __str__(self):
        return f"Team {self.year}"


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='players/photos/', null=True, blank=True)  # поле для фотографии
    number = models.IntegerField(null=True, blank=True)  # поле для номера игрока
    full_birth_date = models.DateField(null=True, blank=True)  # поле для полной даты рождения

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

