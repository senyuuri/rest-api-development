from django.contrib.auth.models import User
from rest_framework import serializers
from apiapp.models import Diary, Profile

class DiarySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Diary
        fields = ['id', 'title', 'author', 'publish_date', 'public', 'text']


class UserSerializer(serializers.ModelSerializer):
    diary = serializers.PrimaryKeyRelatedField(many=True, queryset=Diary.objects.all())
    fullname = serializers.CharField(source='profile.fullname')
    uuid = serializers.ReadOnlyField(source='profile.uuid')

    class Meta:
        model = User
        fields = ('id', 'username', 'fullname', 'uuid','diary')