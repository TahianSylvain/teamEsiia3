# from django.contrib.auth.mixins import LoginRequiredMixin
# from trace import CoverageResults

# from axes.decorators import axes_dispatch
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
# from django.urls import reverse_lazy
# from django.views.generic import TemplateView

from accounts.models import Student, Teacher
from course.forms import CourseForm
from course.models import Attendance, Subject, Course

# from department.models import Level
from department.models import Department


def homeindex(request):
    depts = Department.objects.all()
    tab = []
    # print(type(depts))
    for dept in depts:
        dic = {
            'obj': dept,
            'url': dept.dept_cover.url,
        }
        tab.append(dic)
    return render(request, 'base/index.html', context={'depts': tab})


# class Home(LoginRequiredMixin, TemplateView):
#     template_name = "base/home.html"
#     def get_template_names(self):
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         if user.type == "STUDENT":
#             context['student'] = Student.objects.get(pk=user.pk)
#             context['subjects'] = context['student'].dept.subject_set.all()
#         elif user.type == "TEACHER":
#             context['teacher'] = Teacher.objects.get(pk=user.pk)
#         return context

@login_required
def home(request):
    global template, context, subject_add_course
    user = get_user(request)
    if user.type == "STUDENT":
        student = Student.objects.get(pk=user.pk)
        # subjects = student.dept.subject_set.all()
        subjects = Subject.objects.filter(dept=student.dept)
        course_in_dept = Course.objects.filter(dept=student.dept).order_by('-date_upload')

        # print(course_in_dept)
        # NEW COURSES
        attendance = Attendance.objects.filter(student=student)
        new_course = []
        for attend in attendance:
            for course in course_in_dept:
                if attend.course == course:
                    continue
                else:
                    new_course.append(course)

        courses = Course.objects.filter(dept=student.dept).order_by('-date_upload')
        all_course = []
        for course in courses:
            try:
                attendance = Attendance.objects.get(course=course, student=student)
            except:
                attendance = False

            if attendance:
                attendance_state = attendance.state
            else:
                attendance_state = False
            data_course = {
                'title': course.title,
                'slug': course.slug,
                'subject_slug': course.subject.subject_slug,
                'date': course.date_upload.strftime('%d %B %Y'),
                'hour': course.date_upload.strftime('%H:%M'),
                'presence': attendance_state,
            }
            all_course.append(data_course)
        """ -------------------------------------------------------- """

        template = "accounts/stu_home.html"
        context = {
            'student': student,
            'subjects': subjects,
            'new_courses': new_course,
            'courses': all_course,
        }

        # COURSE LIST IN SUBJECT
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = request.GET.get('data')
            subject = Subject.objects.filter(subject_name=data, dept=student.dept)
            courses = Course.objects.filter(subject=subject[0])
            courses = courses.order_by('-date_upload')
            res = []
            for course in courses:
                url_detail = f'/course/{subject[0].subject_slug}/{course.slug}'
                try:
                    attendance = Attendance.objects.get(course=course, student=student)
                except:
                    attendance = False

                if attendance:
                    attendance_state = attendance.state
                else:
                    attendance_state = False

                data = {
                    'title': course.title,
                    'url_detail': url_detail,
                    'subject': subject[0].subject_name,
                    'date_upload': course.date_upload.strftime('%d %b %Y'),
                    'hour_upload': course.date_upload.strftime('%H:%M'),
                    'present': attendance_state,
                }

                res.append(data)
            return JsonResponse({'data_res': res})
        # return render(request, template, context=contex!)
        """ ------------------------------------------------------------------------ """

    elif user.type == "TEACHER":
        teacher = Teacher.objects.get(pk=user.pk)
        subjects = Subject.objects.filter(teacher=teacher)
        all_course = Course.objects.filter(teacher=teacher).order_by('-date_upload')

        depts = []
        for sub in subjects:
            dept_dic = {
                'name': sub.dept,
                'slug': sub.dept.dept_slug,
                'cover_url': sub.dept.dept_cover.url,
                'nbr_stu': len(Student.objects.filter(dept=sub.dept))
            }
            if dept_dic not in depts:
                depts.append(dept_dic)

        courses = []
        for course in all_course:
            url_detail = f'/course/{course.subject.subject_slug}/{course.slug}'
            course_dic = {
                'title': course.title,
                'date': course.date_upload.strftime('%d %b %Y'),
                'hour': course.date_upload.strftime('%H:%M'),
                'url': url_detail,
            }
            courses.append(course_dic)

        template = "accounts/tea_home.html"
        context = {
            'teacher': teacher,
            'depts': depts,
            'courses': courses,
        }

        # SHOW SUBJECTS IN DEPT
        if request.method == 'GET' and 'data' in request.GET:
        # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dept = Department.objects.get(dept_slug=request.GET.get('data'))
            subjects = Subject.objects.filter(dept=dept, teacher=teacher)

            res = []
            for subject in subjects:
                data = {
                    'subject_name': subject.subject_name,
                    'subject_slug': subject.subject_slug,
                }
                res.append(data)
            # res.append({'subject_name':'test'})
            return JsonResponse({'subject_res': res})

        # SHOW COURSES IN SUBJECT
        if request.method == 'GET' and 'sbj' in request.GET:
            subject = Subject.objects.get(subject_name=request.GET.get('sbj'))
            subject_add_course = subject
            courses = Course.objects.filter(subject=subject).order_by('-date_upload')
            dept = Department.objects.get(dept_title=subject.dept.dept_title).dept_title
            # print(courses)
            res = []
            for course in courses:
                url_detail = f'/course/{course.subject.subject_slug}/{course.slug}'
                data = {
                    'title': course.title,
                    'date': course.date_upload.strftime("%d %b %Y"),
                    'hour': course.date_upload.strftime("%H:%M"),
                    'dept': course.dept.dept_title,
                    'url': url_detail,
                }
                res.append(data)

            return JsonResponse({'courses_res': res, 'dept': dept})

        # CREATE COURSE
        # if request.method == 'GET' and 'subject_add_course' in request.GET:
        #     print('eeeeeeeeee')
        #     subject_add_course = Subject.objects.get(subject_name=request.GET.get('subject_add_course'))
        if request.method == 'POST':
            print(f'==>{request.POST}')
            new_course = CourseForm(request.POST, request.FILES)
            if new_course.is_valid():
                # print(f'=>{new_course}')
                new_course = new_course.save(commit=False)
                new_course.subject = subject_add_course
                print(new_course)
                new_course.save()

            else:
                print("eee")

        context['form'] = CourseForm()
        return render(request, template, context=context)

    else:
        return redirect("admin")
    return render(request, template, context=context)
