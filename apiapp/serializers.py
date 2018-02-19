from rest_framework import serializers
from apiapp.models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'publish_date', 'public', 'text']
