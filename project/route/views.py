from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest


def index(request):
    login = request.GET.get('login', 'Логина нет')
    password = request.GET.get('password', 'Пароля нет')

    return HttpResponse(f'Главная страница <br> Ваш логин: {login} <br> Ваш пароль: {password}')
    # return HttpResponseRedirect('/route/about')
    # return HttpResponsePermanentRedirect('/route/contacts')


def access(request):
    login = request.GET.get('login', 'no')
    password = request.GET.get('password', 'no')
    if login and password == 'admin':
        return HttpResponse('Все ок, доступ разрешен')
    else:
        return HttpResponseNotFound('Доступ запрещен')



def error(request):
    return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')


def about(request):
    return HttpResponse('Данный о нас.')


def contacts(request):
    return HttpResponse('Наши контакты.')


def posts(request):
    return HttpResponse('Страница постов')


def post(request, id):
    return HttpResponse(f'Последняя страница поста №: {id}')


def info(request, id):
    comments = request.GET.get('comments', 0)
    likes = request.GET.get('likes', 0)
    return HttpResponse(f"У поста {id}: <br>{comments} комментариев <br> {likes} лайков")