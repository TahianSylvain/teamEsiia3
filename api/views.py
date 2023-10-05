from django.shortcuts import render
from course.models import Subject
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['GET', "POST", "PUT"])
def prof_api(request):
    temp = Subject.objects.all()
    return Response({"message": "Hello World!", "temp": temp})
