from django.shortcuts import render
from course.models import Subject
from .serializers import SubjectSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['GET', "POST", "PUT"])
def prof_api(request):
    if request.method == 'GET':
        query = Subject.objects.all()
        temp = SubjectSerializer(query, many=True)
        return Response( { 'message': 'GET request received',
            "temp": temp.data
            },
                         status=status.HTTP_200_OK)

    if request.method == 'POST':
        # Handle POST request logic here
        return Response({'message': 'POST request received'},
                         status=status.HTTP_201_CREATED)

    if request.method == 'PUT':
        # Handle PUT request logic here
        return Response({'message': 'PUT request received'},
                         status=status.HTTP_200_OK)

    # Handle unsupported HTTP methods
    return Response({'message': 'Unsupported method'}, 
                     status=status.HTTP_405_METHOD_NOT_ALLOWED)
