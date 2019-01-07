from django.http import HttpResponse
from django.shortcuts import render


def test(request, number=None):
    return HttpResponse('OK %s' % number)
