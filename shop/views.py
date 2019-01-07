from django.http import HttpResponse
from django.shortcuts import render


def test(request, name):
    return HttpResponse('OK {}'.format(name))
