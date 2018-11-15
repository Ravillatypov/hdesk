from django.shortcuts import render, redirect
from account.models import Account
from django.contrib.auth import authenticate, login, logout
from article.views import getBaseContext
from django.contrib.auth.models import User


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


def registerPage(request):
    context = getBaseContext()
    if request.method == 'GET':
        return render(request, 'register.html', context=context)
    if request.method == 'POST':
        username = request.POST.get('login')
        passwd = request.POST.get('password')
        first = request.POST.get('firstname')
        last = request.POST.get('lastname')
        u, created = User.objects.get_or_create(username=username)
        if created:
            u.set_password(passwd)
            u.first_name = first
            u.last_name = last
            u.save()
            return redirect('/login')
        context.update({'error': True, 'login': username,
                        'first': first, 'last': last})
        return render(request, 'register.html', context=context)
