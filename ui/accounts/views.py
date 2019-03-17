from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'accounts/login.html')

def signup(request):
    form = UserCreationForm
    return render(request, 'accounts/signup.html', {'title': 'Sign Up'}, {'form': form})
