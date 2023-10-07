from django.urls import path
from smtp.views import smtp_func 
from base.views import home, landing_views, institut_list

urlpatterns = [
    path('',
             landing_views,
                     name='index'),
    path('home/', home, name='home'),
    path('smtp/', smtp_func, name='mailing'), 
    path('institut/', institut_list, name='institut')
]
