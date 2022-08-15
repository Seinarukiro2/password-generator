from curses.ascii import isupper
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'password_creator/index.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('symbols'):
        characters.extend(list('!@#$%^&*-_'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    yourPassword = ''
    for i in range(length):
        yourPassword += random.choice(characters)
    return render(request, 'password_creator/password.html', {'password': yourPassword})


