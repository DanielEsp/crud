from django.shortcuts import redirect, render
from .models import User
from .forms import UserForm

# Create your views here.
def user(request):
    users = User.objects.all()
    context = {'users' : users}
    return render(request, 'Users/main_user.html', context)

def add(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_user')
    else:
        form = UserForm()
    
    context = {'userform' : form}
    return render(request, 'Users/add_user.html', context)

def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('main_user')

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('main_user')
    else:
        form = UserForm(instance=user)

    context = {"userform" : form}
    return render(request, "Users/edit_user.html", context)