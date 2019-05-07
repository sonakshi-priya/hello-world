from django.urls import path

from . views import homePageView, aboutPageView, contactPageView

urlpatterns = [
    path('',homePageView),
    path('about/', aboutPageView),
    path('contact/', contactPageView),
]