from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework import generics
from apiapp.models import Diary
from apiapp.serializers import DiarySerializer, UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DiaryList(generics.ListCreateAPIView):
    """Return a list of diary entries. Support GET/POST."""
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

    def list(self, request, *args, **kwargs):
        """Override the default list method to add custom fields to the response data."""
        response = super(DiaryList, self).list(request, *args, **kwargs) 
        response.data = {
            'status': True,
            'result': response.data
        }
        return response

    def perform_create(self, serializer):
        """Add author info to a diary."""
        serializer.save(author=self.request.user)


class DiaryDetail(generics.RetrieveUpdateDestroyAPIView):
    """Return the detail of a diary. Support GET/PUT/DELETE"""
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
