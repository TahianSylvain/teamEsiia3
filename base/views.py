from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from department.models import Department
from .home_views import student_home, prof_home
from base.models import Institut
from course.models import Subject


def landing_views(request):
    depts = Department.objects.all()
    tab = []
    for dept in depts:
        dic = {
            'obj': dept,
            'url': dept.dept_cover.url,
        }
        tab.append(dic)
    return render(request, 'base/landing_page.html', context={'depts': tab})


@login_required
def home(request):
    global template, context, subject_add_course
    user = get_user(request)
    subject = Subject.objects.get(id=3)     ## get(subject_name=request.GET.get('sbj'))
    dept = Department.objects.get(dept_title=subject.dept.dept_title).dept_title
    if user.type == "STUDENT":
        print('student')
        return student_home(request=request , user = user, dept=dept)

    elif user.type == "TEACHER":
        print('teacher')
        return prof_home(request=request, user=user, dept=dept)

    else:
        return redirect("admin")


def institut_list(request,*args, **kwargs):
    institut = Institut.objects.all()
    context = {
        'institut':institut
    }
    return render(request, 'base/institut.html', context)