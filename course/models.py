from django.db import models
from django.db.models import SET_NULL
from django.utils.text import slugify
from django.utils.timezone import now
from accounts.models import MyUser, Teacher, Student
from department.models import Department


class Subject(models.Model):
    subject_name = models.CharField('subject', max_length=100, blank=False)
    subject_slug = models.SlugField()
    dept = models.ForeignKey(Department, verbose_name='subject department', on_delete=models.CASCADE, blank=False)
    teacher = models.ForeignKey(Teacher, verbose_name='teacher', on_delete=models.CASCADE, blank=False)
    objects = models.Manager

    def __str__(self):
        return self.subject_name

    def save(self, *args, **kwargs):
        if not self.subject_slug:
            self.subject_slug = slugify(self.subject_name)
        return super().save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField('title', max_length=100, blank=False)
    slug = models.SlugField()
    description = models.TextField('desc', blank=False)
    video = models.FileField(upload_to='courses/video', blank=True, null=True)
    date_upload = models.DateTimeField("date upload", auto_now=True, blank=False, null=False)
    subject = models.ForeignKey(Subject, verbose_name="subject", on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, verbose_name="teacher", on_delete=models.CASCADE, blank=True, null=True)
    objects = models.Manager

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            self.dept = self.subject.dept
            self.teacher = self.subject.teacher
        return super().save(*args, **kwargs)


class AdviseFromPeople(models.Model):
    # avatar = models.URLField()
    objects = models.Manager()
    mess = models.TextField(default='')
    threads = models.ForeignKey(to=Course, on_delete=models.SET_NULL, null=True, blank=False)
    one = models.ForeignKey(to=MyUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.mess}'


class Attendance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    state = models.BooleanField(blank=False, null=False, default=False)
    objects = models.Manager

    def __str__(self):
        return f'{self.course}--{self.student}--{self.state}'

