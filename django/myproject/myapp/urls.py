from django.urls import path
from .views import login_view, logout_view, guest_login, submit_score, leaderboard


app_name = 'myapp'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('guest_login/', guest_login, name='guest_login'),
    path('submit_score/', submit_score, name='submit_score'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]
