from django.contrib import admin
from course.models import Subject, Course, AdviseFromPeople, Attendance


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'teacher', 'dept',)
    search_fields = ('teacher', )
    # autocomplete_fields = ('teacher', 'dept',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'teacher')
    search_fields = ('title', 'subject', 'teacher',)
    autocomplete_fields = ('subject', 'teacher', 'dept',)


@admin.register(AdviseFromPeople)
class AdviseFromPeopleAdmin(admin.ModelAdmin):
    list_display = ('mess',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'state')
    # search_fields = ('course', 'student', 'state')
    # autocomplete_fields = ('course', 'student')
