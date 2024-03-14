from django.http import HttpResponse


def index(request):
    return HttpResponse('FIRST PAGE')


def second_page(request):
    return HttpResponse('SECOND PAGE')
