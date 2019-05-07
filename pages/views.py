
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')


def aboutPageView (request):
    return HttpResponse ('About')


def contactPageView (request):
    return HttpResponse ('Contact')
