from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from apiapp.models import Diary, Profile, UserToken


class DiarySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Diary
        fields = ['id', 'title', 'author', 'publish_date', 'public', 'text']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['fullname']


class ProfileCreationSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField()
    age = serializers.IntegerField()

    class Meta:
        model = Profile
        fields = ['fullname', 'age']


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['username', 'password', 'fullname', 'age']
        write_only_fields = ['password']

    def create(self):
        profile = {'fullname': self.validated_data.pop('fullname'),
                   'age': self.validated_data.pop('age')}
        user = User.objects.create(**self.validated_data)
        Profile.objects.create(user=user, **profile)


class UserAuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')

    def user(self):
        username = self.validated_data['username']
        password = self.validated_data['password']
        user = User.objects.get(username=username)
        if user is not None and password == user.password:
            return user
        else:
            return None


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = UserToken
        fields = ('token',)

    def create(self, user):
        UserToken.objects.create(user=user, **self.validated_data)

    def delete(self):
        try:
            instance = UserToken.objects.get(token=self.validated_data['token'])
            instance.delete()
            return True
        except ObjectDoesNotExist as e:
            return False
        return False

    def get_user(self):
        try:
            instance = UserToken.objects.get(token=self.validated_data['token'])
            return instance.user
        except ObjectDoesNotExist as e:
            return None
        return None


class DiaryCreateSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = Diary
        fields = ['title', 'publish_date', 'public', 'text', 'token']

    def validate_token_exists(self, data):
        serializer = TokenSerializer(data=data['token'])
        if serializer.is_valid():
            user = serializer.get_user()
            if user is None:
                raise serializers.ValidationError("Invalid token")

    def create(self):
        try:
            instance = UserToken.objects.get(token=self.validated_data['token'])
            user = instance.user
        except ObjectDoesNotExist as e:
            return None
        data = self.validated_data
        data.pop('token')
        diary = Diary.objects.create(author=user, **data)
        return diary.id


class DiaryModifySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    private = serializers.BooleanField(default=True)
    token = serializers.CharField()

    class Meta:
        model = UserToken
        fields = ['id', 'token', 'private']

    def validate_token_exists_and_ownership(self, data):
        serializer = TokenSerializer(data=data['token'])
        if serializer.is_valid():
            user = serializer.get_user()
            if user is None:
                raise serializers.ValidationError("Invalid token")
            else:
                try:
                    Diary.objects.filter(author=user).get(id=data['id'])
                except ObjectDoesNotExist as e:
                    raise serializers.ValidationError("Invalid diary id")

    def delete(self):
        try:
            instance = UserToken.objects.get(token=self.validated_data['token'])
            user = instance.user
        except ObjectDoesNotExist as e:
            return None
        diary = Diary.objects.filter(author=user).get(id=self.validated_data['id'])
        diary.delete()
        return True

    def update_permission(self):
        try:
            print(self.validated_data)
            instance = UserToken.objects.get(token=self.validated_data['token'])
            user = instance.user
            diary = Diary.objects.filter(author=user).get(id=self.validated_data['id'])
            diary.public = not self.validated_data['private']
            diary.save()
            return True
        except ObjectDoesNotExist as e:
            return False
