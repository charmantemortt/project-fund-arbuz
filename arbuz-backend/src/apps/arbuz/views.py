from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Forms, News
from .serializers import ProjectSerializer, FormsSerializer, NewsSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class FormsViewSet(viewsets.ModelViewSet):
    queryset = Forms.objects.all()
    serializer_class = FormsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project_id = serializer.validated_data['project'].id
        project = Project.objects.get(id=project_id)

        project.current_amount += serializer.validated_data['sum']
        project.save()

        form = Forms.objects.create(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer