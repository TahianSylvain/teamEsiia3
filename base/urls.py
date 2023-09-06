from django.urls import path

from base.views import home, landing_views, institut_list

urlpatterns = [
    path('', landing_views, name='index'),
    path('home/', home, name='home'),
    path('institut/', institut_list, name='institut')
]
