from django.shortcuts import render
from course.models import Subject
from .serializers import SubjectSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import Group
from accounts.models import Student, MyUser
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import StudentSerializer# , GroupSerializer
from django.contrib.auth import authenticate


class UserCreate(generics.CreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = ()
    serializer_class = StudentSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all().order_by('-date_joined')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

"""
from rest_framework.exceptions import PermissionDenied

class PollViewSet(viewsets.ModelViewSet):
    def destroy(self, request, *args, **kwargs):
        obj = Obj.objects.get(pk=self.Kwargs['pk'])
        if not request.user == poll.created_by:
            raise PermissionDenied('You cannot delete this!')
        reutrn super().destroy(request,  *args, **kwargs)

class ChoiceList(generics.ListCreateView):
    def post(self, request,  *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs['uuid'])
        if not request.user == poll.created_by:
            raise PermissionDenied('This is not yours')
        return super().post(request,  *args, **kwargs)
"""

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
