from django.urls import path
from .views import prof_api


urlpatterns = [
    path("for-a-prof/", prof_api),
]