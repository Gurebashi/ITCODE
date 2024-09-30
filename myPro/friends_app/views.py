from django.http import HttpResponse
from django.shortcuts import render


def myfriends(request):
    return HttpResponse("Мои друзья")


def groupfriends(request):
    return HttpResponse('Общие друзья в группе "Джанго" ')


def recfriends(request):
    return HttpResponse("Рекомендованные друзья")
