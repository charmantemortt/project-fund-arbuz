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
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        Forms.objects.create_form(
            sum=serializer.validated_data['sum'],
            pay_status=serializer.validated_data['pay_status'],
            user_name=serializer.validated_data['user_name'],
            comment=serializer.validated_data['comment'],
            link_status=serializer.validated_data['link_status'],
            link_field=serializer.validated_data['link_field']
        )

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer