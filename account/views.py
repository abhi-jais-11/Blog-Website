from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from .forms import UserRegisterForm
from django.contrib import messages

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})
        
    
    
    
def LoginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            return redirect('/')
        
    form = AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'account/login.html',context)


def LogoutView(request):
    logout(request)
    return redirect('/')


