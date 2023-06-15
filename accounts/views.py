from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

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
