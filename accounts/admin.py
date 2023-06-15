from django.contrib import admin

from accounts.models import MyUser, Student, Teacher


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "type",
        "sex"
    )
    search_fields = ("username", "type", "sex")
    # autocomplete_fields = ("type", )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "dept",
        "type",
        "sex",
    )
    search_fields = ("username", "dept", "sex")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "type",
        "sex",
    )
    search_fields = ('username', "sex")
