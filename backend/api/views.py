from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Profile, Company, Experience, Project, Skill, ContactMessage
from .serializers import (
    ProfileSerializer, 
    CompanySerializer, 
    ExperienceSerializer, 
    ProjectSerializer, 
    SkillSerializer,
    ContactMessageSerializer
)

@method_decorator(cache_page(60*15), name='list')
@method_decorator(cache_page(60*15), name='retrieve')
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.prefetch_related('languages').all()
    serializer_class = ProfileSerializer

@method_decorator(cache_page(60*15), name='list')
@method_decorator(cache_page(60*15), name='retrieve')
class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.prefetch_related('experiences').all()
    serializer_class = CompanySerializer

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

@method_decorator(cache_page(60*15), name='list')
@method_decorator(cache_page(60*15), name='retrieve')
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.prefetch_related('images').all()
    serializer_class = ProjectSerializer

@method_decorator(cache_page(60*15), name='list')
@method_decorator(cache_page(60*15), name='retrieve')
class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from rest_framework.permissions import AllowAny, IsAdminUser

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def get_permissions(self):
        """
        Allow anyone to POST (send logs), but only Admin can GET (view logs).
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        # Save the message to DB
        message_obj = serializer.save()
        
        # Try to send an email notification
        try:
            subject = f"Portfolio Contact: {message_obj.subject}"
            content = f"Message from: {message_obj.name} ({message_obj.email})\n\n{message_obj.message}"
            
            email = EmailMessage(
                subject,
                content,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                cc=[message_obj.email],
                reply_to=[message_obj.email]
            )
            email.send(fail_silently=False)
            
        except Exception as e:
            # We still return success because it's saved in DB
            print(f"Email failed to send: {e}")

