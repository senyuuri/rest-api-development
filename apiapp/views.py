from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from apiapp.models import Diary
from apiapp.serializers import DiarySerializer

class DiaryList(generics.ListCreateAPIView):
    """Return a list of diary entries. Support GET/POST."""
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class DiaryDetail(generics.RetrieveUpdateDestroyAPIView):
    """Return the detail of a diary. Support GET/PUT/DELETE"""
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer