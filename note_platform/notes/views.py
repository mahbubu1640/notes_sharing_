from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Note, NoteShare
from .serializers import NoteSerializer, NoteShareSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    notes = Note.objects.filter(user=user)
    shared_notes = NoteShare.objects.filter(shared_with=user)
    return render(request, 'profile.html', {'user': user, 'notes': notes, 'shared_notes': shared_notes})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page or any other page after logout



class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteShareViewSet(viewsets.ModelViewSet):
    queryset = NoteShare.objects.all()
    serializer_class = NoteShareSerializer
