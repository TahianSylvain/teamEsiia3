from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy, reverse
from django.views.generic import RedirectView

from accounts.forms import TeacherRegisterForm
from accounts.models import Teacher
from accounts.views import Register, Login

urlpatterns = [
    path('', RedirectView.as_view(url='/admin'), name="admin"),
    path('student-register/<str:dept_slug>', Register.as_view(), name="stu_reg"),
    path(
        'teacher-register/',
        Register.as_view(
            model=Teacher,
            template_name="accounts/tea_reg.html",
            form_class=TeacherRegisterForm,
        ),
        name="tea_reg",
    ),
    path('login/', Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
