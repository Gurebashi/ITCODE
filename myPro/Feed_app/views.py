from django.http import HttpResponse
from django.shortcuts import render

def feed_entrance(request):
    return HttpResponse('Новостная лента')
def group(request):
    return HttpResponse('Лента новостей группы "Джанго"')
def persona(request):
    return HttpResponse('Ваша лента новостей')
