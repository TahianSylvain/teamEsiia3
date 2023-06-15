from django.conf.urls.static import static
from django.urls import path
from course.views import CourseList, course_detail
from lvlind import settings

urlpatterns = [
    path('<str:subject_slug>/', CourseList.as_view(), name="course_list"),
    path('<str:subject_slug>/<str:slug>/', course_detail, name="course_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
