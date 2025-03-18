from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FormsViewSet, NewsViewSet

from .views import ProjectViewSet, FormsViewSet, NewsViewSet

router = DefaultRouter()

router.register(r'projects', ProjectViewSet)
router.register(r'forms', FormsViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]