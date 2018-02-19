from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apiapp.models import Diary
from apiapp.serializers import DiarySerializer
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST'])
@csrf_exempt
def diary_list(request, format=None):
    """List all diarys, or create a new diary."""
    if request.method == 'GET':
        diaries = Diary.objects.all()
        serializer = DiarySerializer(diaries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def diary_detail(request, pk, format=None):
    """Retrieve, update or delete a diary."""
    try:
        diary = Diary.objects.get(pk=pk)
    except Diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiarySerializer(diary)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiarySerializer(diary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        diary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)