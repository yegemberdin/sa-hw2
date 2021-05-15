from django.shortcuts import render, redirect
from .models import User
from .forms import UserForms


# Create your views here.
def list_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def create_user(request):
    form = UserForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'users-form.html', {'form': form})


def update_user(request, id):
    user = User.objects.get(id=id)
    form = UserForms(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'users-form.html', {'form': form, 'user': user})


def delete_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('list_users')
    return render(request, 'user-delete-confirm.html', {'user': user})
