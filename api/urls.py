from django.urls import path, include
from .views import UserCreate, prof_api, UserViewSet#, GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',  UserViewSet)
# router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('student_creation/', UserCreate.as_view()),
    path('api-auth/', 
        include('rest_framework.urls',namespace='rest_framework')
    ),
    path("for-a-prof/", prof_api),
]