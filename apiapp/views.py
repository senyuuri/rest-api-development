from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import generics
from apiapp.models import Diary, Profile, UserToken
from apiapp.serializers import (
    DiarySerializer, UserSerializer, TokenSerializer, UserCreateSerializer,
    UserAuthSerializer, TokenSerializer, DiaryCreateSerializer,
    DiaryModifySerializer)
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def user_list(request):
    """
    @brief      List fullnames of all users
    """
    users = Profile.objects.all().only('fullname')
    serializer = UserSerializer(users, many=True)
    obj = {
        'status': True,
        'result': list(map((lambda x: x['fullname']), serializer.data))
    }
    return Response(obj)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def heartbeat(request):
    return Response({'status': True})


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def endpoints(request):
    return Response({'status': True,
                    'result': [
                        '/',
                        '/meta/heartbeat',
                        '/meta/team',
                        '/users/register',
                        '/users/authenticate',
                        '/users/expire',
                        '/users',
                        '/diary',
                        '/diary/create',
                        '/diary/delete',
                        '/diary/permission'
                    ]})


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def user_register(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.create()
            return Response({'status': True},
                            status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({'status': False, 'error': 'User already exists!'})
    else:
        return Response({'status': False})


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def user_auth(request):
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.user() is not None:
            token = UserToken.objects.create(user=serializer.user())
            return Response({'status': True,
                             'token': token.token})
    return Response({'status': False})


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def token_exp(request):
    serializer = TokenSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.delete():
            return Response({'status': True})
    return Response({'status': False})


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def user_detail(request):
    serializer = TokenSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.get_user()
        if user is not None:
            return Response({
                'status': True,
                'username': user.username,
                'fullname': user.profile.fullname,
                'age': user.profile.age
                })
    return Response({'status': False})


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def list_diaries(request):
    if request.method == 'GET':
        diaries = Diary.objects.filter(public=True)
        serializer = DiarySerializer(diaries, many=True)
        obj = {
            'status': True,
            'result': serializer.data
        }
        return Response(obj)
    elif request.method == 'POST':
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.get_user()
            if user is not None:
                diaries = Diary.objects.filter(author=user)
                serializer = DiarySerializer(diaries, many=True)
                obj = {
                    'status': True,
                    'result': serializer.data
                }
                return Response(obj)


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def create_diary(request):
    serializer = DiaryCreateSerializer(data=request.data)
    if serializer.is_valid():
        result = serializer.create()
        if result is not None:
            return Response({'status': True, 'result': result},
                            status=status.HTTP_201_CREATED)
    return Response({'status': False, "error": "Invalid authentication token."})


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def delete_diary(request):
    serializer = DiaryModifySerializer(data=request.data)
    if serializer.is_valid():
        result = serializer.delete()
        if result is not None:
            return Response({'status': True, 'result': result})
    Response({'status': False, "error": "Invalid authentication token."})


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def update_diary(request):
    serializer = DiaryModifySerializer(data=request.data)
    if serializer.is_valid():
        result = serializer.update_permission()
        if result:
            return Response({'status': True})
    return Response({'status': False})
