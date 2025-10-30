from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model
class User(AbstractUser):
    is_player = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Team model
class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)
    city = models.CharField(max_length=100)
    total_wins = models.IntegerField(default=0)
    total_losses = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Player model
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    matches_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    attendance = models.FloatField(default=0.0)
    performance_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username


# Match model
class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='wins_in')
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team1} vs {self.team2}"


# Attendance model
class Attendance(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='attendance_records')
    session_date = models.DateField()
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player.user.username} - {self.session_date}"


# Leaderboard model
class Leaderboard(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    total_score = models.FloatField(default=0.0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.user.username} - Rank {self.rank}"
