from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("Введите логин")


def register(request):
    return HttpResponse("Регистрация")


def passwordrecover(request):
    return HttpResponse("Забыли пароль?")
