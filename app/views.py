from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import func
# Create your views here.


def test(request):
    func.delay()
    return HttpResponse("Text only, please.", content_type="text/plain")

def test2(request):
    for i in range(100000):
        print(i)
    return HttpResponse("TEST 2 DONE ON DJANGO THREAD")