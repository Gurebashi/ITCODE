from django.http import HttpResponse
from django.shortcuts import render

def myfriends(request):
    return HttpResponse('Мои друзья')

