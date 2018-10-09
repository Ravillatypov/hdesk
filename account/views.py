from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    error = ''
    if request.method == 'GET':
        nextPage = request.GET.get('next')
        if nextPage is None:
            nextPage = '/' 
        return render(request, 'login.html', {'next': nextPage})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nextPage = request.POST.get('next')
        if nextPage is None:
            nextPage = '/' 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(nextPage)
        else:
            error = 'Авторизация не пройдена. Не правильный логин или пароль.'
    return render(request, 'error.html', {'error': error})


def logoutPage(request):
    logout(request)
    return redirect('/')