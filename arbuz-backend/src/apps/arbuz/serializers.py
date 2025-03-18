from pydantic.functional_serializers import ModelSerializer
from models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', ]