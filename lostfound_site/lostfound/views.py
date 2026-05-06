from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import LostItem, FoundItem
from .forms import LostItemForm, FoundItemForm, RegisterForm


# ---------------- HOME ----------------
def home(request):
    return render(request, 'home.html')


# ---------------- REGISTER ----------------
def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'register.html', {'form': form})


# ---------------- LOGIN ----------------
def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')

    return render(request, 'login.html', {'form': form})


# ---------------- LOGOUT ----------------
def user_logout(request):
    logout(request)
    return redirect('home')


# ---------------- ADD LOST ----------------
@login_required
def add_lost(request):
    form = LostItemForm(request.POST or None)

    if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user   # 🔥 attach owner
        item.save()
        return redirect('home')

    return render(request, 'add_lost.html', {'form': form})


# ---------------- ADD FOUND ----------------
@login_required
def add_found(request):
    form = FoundItemForm(request.POST or None)

    if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user   # 🔥 attach owner
        item.save()
        return redirect('home')

    return render(request, 'add_found.html', {'form': form})

@login_required
def my_items(request):
    lost_items = LostItem.objects.filter(user=request.user)
    found_items = FoundItem.objects.filter(user=request.user)

    return render(request, 'my_items.html', {
        'lost_items': lost_items,
        'found_items': found_items
    })


# ---------------- VIEW ITEMS ----------------
def view_items(request):
    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()

    return render(request, 'view_items.html', {
        'lost_items': lost_items,
        'found_items': found_items
    })


def search_items(request):
    query = request.GET.get('q')

    lost_results = []
    found_results = []

    if query:
        lost_results = LostItem.objects.filter(
            Q(type__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        )

        found_results = FoundItem.objects.filter(
            Q(type__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(contact__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, 'search.html', {
        'lost_results': lost_results,
        'found_results': found_results,
        'query': query
    })