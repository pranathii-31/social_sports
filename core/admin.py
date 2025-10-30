from django.contrib import admin
from .models import User, Team, Player, Match, Attendance, Leaderboard

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_player', 'is_coach', 'is_admin')
    list_filter = ('is_player', 'is_coach', 'is_admin')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'total_wins', 'total_losses')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'matches_played', 'wins', 'losses', 'attendance', 'performance_score')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'date', 'winner', 'team1_score', 'team2_score')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('player', 'session_date', 'attended')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('player', 'total_score', 'rank')
