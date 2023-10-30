from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models
from department.models import Department


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("email is required")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.type = user.base_type
        # user.type = type
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField("Username", max_length=50, blank=False, unique=True)
    first_name = models.CharField("First Name", max_length=100, blank=True)
    last_name = models.CharField("Last Name", max_length=100, blank=True)
    date_of_birth = models.DateField("Date of Birth", auto_now_add=False, blank=True, null=True)
    email = models.EmailField("Email Address", blank=False, unique=True)
    pdp = models.ImageField(upload_to="users/profile", blank=True, null=True)

    sex_choice = [
        ('M', "Male"),
        ('F', "Female"),
    ]

    sex = models.CharField(max_length=1, choices=sex_choice, blank=True, default='M')

    class Type(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        STUDENT = "STUDENT", 'Student'
        TEACHER = "TEACHER", 'Teacher'

    base_type = Type.ADMIN
    type = models.CharField(max_length=50, choices=Type.choices)

    date_joined = models.DateTimeField("date joined", auto_now_add=True)
    last_login = models.DateField("last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", )

    objects = MyUserManager()

    def __str__(self):
        return self.username 

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.type = self.base_type
    #         return super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'


# class StudentManager(MyUserManager, models.Manager):
#     def create_user(self, username, email, password=None, type=MyUser.Type.STUDENT):
#         if not email:
#             raise ValueError("email is required")
#
#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#         )
#         user.set_password(password)
#         user.type=type
#         user.save(using=self._db)
#         return user


class Student(MyUser):
    dept = models.ForeignKey(Department, verbose_name="department", on_delete=models.CASCADE, blank=False)
    base_type = MyUser.Type.STUDENT
    account_id = models.PositiveBigIntegerField(unique_for_year=True, null=True)
    visa = models.IntegerField( null=False, blank=False, default=0)

    # objects = StudentManager()


class Teacher(MyUser):
    base_type = MyUser.Type.TEACHER
