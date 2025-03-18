from rest_framework import serializers
from .models import Project, Forms, News

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'description', 'image')

class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms
        fields = ('sum', 'pay_status', 'user_name', 'comment', 'link_status', 'link_field')

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('name', 'description', 'created_at')