from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Service
from .forms import CustomUserCreationForm

User = get_user_model()

def home_view(request):
    latest_services = Service.objects.filter(is_active=True)[:5]
    context = {
        'latest_services': latest_services,
    }
    return render(request, 'online_shop/home.html', context)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'online_shop/register.html', {'form': form})
    
class CustomLoginView(LoginView):
    template_name = 'online_shop/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'

class CustomLogoutView(LogoutView):
    next_page = '/'

@login_required
def profile_view(request):
    return render(request, 'online_shop/profile.html', {'user':request.user})





