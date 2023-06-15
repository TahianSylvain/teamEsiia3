from django.contrib.auth.forms import UserCreationForm
from accounts.models import Student, Teacher


class StudentRegisterForm(UserCreationForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "sex",
            "username",
            "email",
        ]


class TeacherRegisterForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = [
            "first_name",
            "last_name",
            "sex",
            "username",
            "email",
        ]
