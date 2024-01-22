from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserScoreForm
from .models import UserScore

#login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your home page
        else:
            # Handle invalid login
            pass
    return render(request, 'login.html')

#logout 
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page

#guest login(data not being saved)
def guest_login(request):
    # Check if a guest user already exists, create one if not
    guest_username = 'guest_user'
    guest_password = 'guest_password'

    try:
        guest_user = User.objects.get(username=guest_username)
    except User.DoesNotExist:
        guest_user = User.objects.create_user(username=guest_username, password=guest_password)

    login(request, guest_user)
    return redirect('home')  # Redirect to your home page

#scoredata 
def submit_score(request):
    if request.method == 'POST':
        form = UserScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.user = request.user
            score.save()
            return redirect('leaderboard')
    else:
        form = UserScoreForm()
    return render(request, 'submit_score.html', {'form': form})

#leaderboard
def leaderboard(request):
    leaderboard_data = UserScore.objects.order_by('-score')[:5]  # Retrieve top 10 scores
    return render(request, 'leaderboard.html', {'leaderboard_data': leaderboard_data})
