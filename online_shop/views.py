from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import Service, Order
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
    orders = Order.objects.filter(user=request.user)
    return render(request, 'online_shop/profile.html', {'user':request.user, 'orders': orders})


def service_list_view(request):
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services,
    }
    return render(request, 'online_shop/service_list.html', context)

def service_detail_view(request, id):
    service = get_object_or_404(Service, id = id, is_active = True)
    context = {
        'service': service,
    }
    return render(request, 'online_shop/service_detail.html', context)

def search_result_view(request):
    query = request.GET.get('q', '')
    services = []
    if query:
        services = Service.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).filter(is_active=True)
    context = {
        'services': services,
        'query': query,
    }
    return render(request, 'online_shop/search_result.html', context)



@login_required
def create_order_view(request, id):
    service = get_object_or_404(Service, id=id, is_active = True)
    order, created = Order.objects.get_or_create(user=request.user, service=service, defaults={'status': 'Ошидание'})
    if created:
        messages.success(request, f"Вы заказали {service.name}")
    else:
        messages.info(request, f"Вы уже заказывали {service.name} ранее")
    return redirect('service_detail', id=service.id)
