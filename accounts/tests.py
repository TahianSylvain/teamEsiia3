from django.test import TestCase
from .models import MyUser, Student, Teacher
from department.models import Department

class UserModelTestCase(TestCase):
    def setUp(self):
        # Create a sample department
        self.department = Department.objects.create(name="Sample Department")

    def test_create_student(self):
        student = Student.objects.create(
            username="student_username",
            email="student@example.com",
            password="student_password",
            dept=self.department,
        )
        self.assertEqual(student.type, MyUser.Type.STUDENT)
        self.assertTrue(student.is_active)
        self.assertFalse(student.is_admin)

    def test_create_teacher(self):
        teacher = Teacher.objects.create(
            username="teacher_username",
            email="teacher@example.com",
            password="teacher_password",
        )
        self.assertEqual(teacher.type, MyUser.Type.TEACHER)
        self.assertTrue(teacher.is_active)
        self.assertFalse(teacher.is_admin)

    def test_user_full_name(self):
        user = MyUser.objects.create(
            username="user_username",
            email="user@example.com",
            password="user_password",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(user.get_full_name(), "Doe John")

    def test_user_string_representation(self):
        user = MyUser.objects.create(
            username="user_username",
            email="user@example.com",
            password="user_password",
            first_name="John",
            last_name="Doe",
        )
        self.assertEqual(str(user), "user_username")

    def test_user_permissions(self):
        user = MyUser.objects.create(
            username="user_username",
            email="user@example.com",
            password="user_password",
        )
        self.assertTrue(user.has_perm("some_permission"))
        self.assertTrue(user.has_module_perms("some_module"))

    def test_student_visa_default_value(self):
        student = Student.objects.create(
            username="student_username",
            email="student@example.com",
            password="student_password",
            dept=self.department,
        )
        self.assertEqual(student.visa, 0)
