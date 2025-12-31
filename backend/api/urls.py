from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, CompanyViewSet, ExperienceViewSet, ProjectViewSet, SkillViewSet, ContactMessageViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contact', ContactMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
