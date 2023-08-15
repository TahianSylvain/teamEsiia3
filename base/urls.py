from django.urls import path, include, reverse
from django.views.generic import RedirectView

from base.views import home, homeindex, institut_list

urlpatterns = [
    # path('', RedirectView.as_view(url=reverse('admin:index')), name="admin"),
    path('', homeindex, name='index'),
    path('home/', home, name='home'),
    path('institut/', institut_list, name='institut')
    # path('home/', Home.as_view(), name="home"),
]
