from course.models import Subject
from rest_framework import serializers
from django.contrib.auth.models import Group
from accounts.models import Student, MyUser
from rest_framework import serializers
from rest_framework.authtoken.models import Token



class SubjectSerializer(
        serializers.ModelSerializer
    ):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(
        serializers.HyperlinkedModelSerializer
    ):
    class Meta:
        model = MyUser
        fields = ['url', 'username', 'email', 'password']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user=Student(
            email=validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


# class GroupSerializer(
#         serializers.HyperlinkedModelSerializer
#     ):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']