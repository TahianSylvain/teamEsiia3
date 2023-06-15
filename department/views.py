from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from accounts.models import Student
from course.models import Subject
from department.models import Department


class DeptDetail(TemplateView):
    template_name = "department/dept_detail.html"

    def get_context_data(self, dept_slug, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = Department.objects.get(dept_slug=dept_slug)
        context['subjects'] = Subject.objects.filter(dept=context['department'], teacher=self.request.user.pk)
        context['students'] = Student.objects.filter(dept=context['department'])
        return context


# def dept_detail(request, dept_slug):
#     teacher = request.user
#     department = dept.objects.get(dept_slug=dept_slug)
#     # subjects = Subject.objects.filter(department=department, teacher=teacher.pk)
#     subjects = department.subject_set.filter(teacher=teacher.pk)
#     students = Student.objects.filter(department=department)
#     context = {"department": department, "subjects": subjects, "students": students}
#     return render(request, "department/dept_detail.html", context=context)
