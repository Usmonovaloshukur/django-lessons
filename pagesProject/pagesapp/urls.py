from django.urls import path

from .views import homePageView, aboutPageView, servicesPageView

urlpatterns = [
    path('services/', servicesPageView.as_view(), name='services'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('', homePageView.as_view(), name='home')
]