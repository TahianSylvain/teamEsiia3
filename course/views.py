from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DetailView, FormView

from accounts.models import Student, MyUser, Teacher
from course.forms import CourseForm
from course.models import Attendance, Course, Subject, AdviseFromPeople
from department.models import Department


class CourseList(LoginRequiredMixin, TemplateView):
    template_name = 'course/course_list.html'

    def get_context_data(self, subject_slug, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = Subject.objects.get(subject_slug=subject_slug)
        context['department'] = context['subject'].dept
        # context['courses'] = Course.objects.filter(subject=context['subject'])
        context['courses'] = context['subject'].course_set.all()
        # print(type(context['courses'][0].date_upload))
        return context


# def course_list(request, slug):
#     subject = get_object_or_404(Subject, subject_slug=slug)
#     return render(request, 'course/course_list.html', context={'subject': subject})


@login_required()
def course_detail(request, subject_slug, slug):
    # global commentary
    global commentary
    commentary = object
    student = object
    subject = Subject.objects.get(subject_slug=subject_slug)
    course_in_subject = Course.objects.filter(subject=subject).order_by('-date_upload')
    # course = Course.objects.filter(slug=slug, subject=subject)
    course = subject.course_set.filter(slug=slug)

    # COMMENT
    thread = AdviseFromPeople.objects.filter(threads=course[0])  # ses commentaires
    if request.method == 'POST' and 'mess' in request.POST:
        coms = request.POST['mess']
        print(coms)
        commentary = AdviseFromPeople.objects.create(mess=coms, threads=course[0], one=request.user)
        commentary.save()

        if commentary.one.pdp:
            url = commentary.one.pdp.url
        elif commentary.one.sex == "M":
            url = '/static/base/img/default/profile-male.jpg'
        else:
            url = '/static/base/img/default/profile-female.jpg'

        data = {
            'one_name': commentary.one.username,
            'pdp': url,
            'mess': commentary.mess,
        }
        # comment = []
        # comment.append(data)
        # print(f'==>{commentary.one.get_full_name()}')

        return JsonResponse({'comment': data})

    if request.user.type == "STUDENT":
        student = Student.objects.get(pk=request.user.pk)

        # PRESENCE
        if request.method == 'POST' and 'state' in request.POST:
            if request.POST['state'] == 'on':
                present = Attendance.objects.create(course=course[0], student=student, state=True)
                present.save()
                # print(present)

    # if request.user.type == "TEACHER":
    #     teacher = Teacher.objects.get(pk=request.user.pk)

    return render(request, 'course/index_video.html', context={
        'subject': subject,
        'course_in_subject': course_in_subject,
        'course': course,
        'student': student,
        'tell_to_public': commentary,
        'threads': thread,
        })


# class CourseCreateView(CreateView):
#     model = Course
#     fields = ('title', 'description',)
#     template_name = "course/create_course.html"
#     success_url = reverse_lazy("course_list_tea")
#
#     def get_context_object_name(self, obj):
#
#     def get_context_data(self, subject_slug, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['subject'] = Subject.objects.get(subject_slug=subject_slug)
#         return context
#
#     def form_valid(self, form):
#         course = form.save(commit=False)
#         course.subject = context['subject']
#         return super().form_valid(form)


def create_course(request, dept_slug, subject_slug):
    # dept = Department.objects.get(dept_slug=dept_slug)
    subject = Subject.objects.get(subject_slug=subject_slug)
    if request.method == "POST":
        course = CourseForm(request.POST, request.FILES)
        if course.is_valid():
            # print(course.cleaned_data)
            course = course.save(commit=False)
            course.subject = subject
            # course.save()
            return redirect(reverse("course_list_tea", kwargs={"dept_slug": dept_slug, "subject_slug": subject_slug}))
    else:
        course = CourseForm()

    return render(request, "course/create_course.html", {"form": course})


#@login_required  # fonction décorateur
#def display_free_courses(request, module_id):
#     global commentary
#     #  stop_recording()
#     user = request.user
#     objectif = Course.objects.get(id=module_id)
#     if user.type == 'student':
#         pass  # nom; date; cours; matiere
#     thread = AdviseFromPeople.objects.filter(threads=objectif)  # ses commentaires
#     if request.method == 'POST':
#         coms = request.POST['mess']
#         commentary = AdviseFromPeople.objects.create(mess=coms, threads=objectif, one=user)
#         commentary.save()
#     return render(request, 'course.html', context={
#             'vue': objectif,
#             'tell_to_public': commentary,
#             'thread': thread,
#         })
