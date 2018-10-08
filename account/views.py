from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    error = False
    if request.method == 'GET':
        nextPage = request.POST.get('next')
        if nextPage is None:
            nextPage = '/'
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
            error = True
    return render(request, 'login.html', {'next': nextPage, 'error': error})


def logoutPage(request):
    logout(request)
    return redirect('/')