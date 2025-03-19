from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FormsViewSet, NewsViewSet

from .views import ProjectViewSet, FormsViewSet, NewsViewSet

router = DefaultRouter()

router.register(r'project', ProjectViewSet)
router.register(r'form', FormsViewSet)
router.register(r'new', NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]