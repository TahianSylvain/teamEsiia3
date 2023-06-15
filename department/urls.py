from django.conf.urls.static import static
from django.urls import path

from course.views import CourseList, create_course
from department.views import DeptDetail
from lvlind import settings

urlpatterns = [
    path('<str:dept_slug>/', DeptDetail.as_view(), name='dept_detail'),  # department detail for teacher
    path(
        '<str:dept_slug>/<str:subject_slug>/',
        CourseList.as_view(
            template_name="course/course_list_tea.html"
        ),
        name="course_list_tea",
    ),
    path('<str:dept_slug>/<str:subject_slug>/new-course/', create_course, name="create_course"),
    # path('<str:dept_slug>/<str:subject_slug/', )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

