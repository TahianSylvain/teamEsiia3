from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
    
from django.urls import reverse
from django.contrib.auth import get_user_model

from accounts.forms import StudentRegisterForm
from accounts.models import Student
from department.models import Department


class Register(CreateView):
    model = Student
    template_name = "accounts/stu_reg.html"
    form_class = StudentRegisterForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sex_choice"] = Student.sex_choice
        if self.kwargs:
            context["dept"] = Department.objects.get(dept_slug=self.kwargs['dept_slug'])
        return context

    def form_valid(self, form):
        # print(form.cleaned_data)
        user = form.save(commit=False)
        user.type = user.base_type
        if user.type == "STUDENT":
            user.dept = Department.objects.get(dept_slug=self.kwargs['dept_slug'])
        return super().form_valid(form)


class Login(LoginView):
    template_name = "accounts/login.html"
    fields = "__all__"

    def get_success_url(self):
        if self.request.user.type == "ADMIN":
            return reverse_lazy("admin")
        return reverse_lazy("home")
    

class RegisterViewTestCase(TestCase):
    def setUp(self):
        # Create a sample department
        self.department = Department.objects.create(name="Sample Department")

    def test_register_view(self):
        # Ensure the register view is accessible
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_register_student(self):
        # Ensure a student can be registered
        data = {
            "username": "student_username",
            "email": "student@example.com",
            "password1": "student_password",
            "password2": "student_password",
            "dept": self.department.pk,
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 302)  # Should redirect after registration
        self.assertTrue(Student.objects.filter(username="student_username").exists())

    def test_register_teacher(self):
        # Ensure a teacher can be registered
        data = {
            "username": "teacher_username",
            "email": "teacher@example.com",
            "password1": "teacher_password",
            "password2": "teacher_password",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 302)  # Should redirect after registration
        self.assertTrue(get_user_model().objects.filter(username="teacher_username").exists())

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
        )

    def test_login_view(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_login_valid_user(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, 302)  # Should redirect after login
        self.assertEqual(response.url, reverse("home"))

    def test_login_admin_user(self):
        self.user.type = Student.Type.ADMIN
        self.user.save()
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, 302)  # Should redirect after login
        self.assertEqual(response.url, reverse("admin"))

    def test_login_invalid_user(self):
        data = {
            "username": "invaliduser",
            "password": "invalidpassword",
        }
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, 200)  # Should stay on the login page

