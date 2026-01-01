from rest_framework import viewsets
from .models import Profile, Company, Experience, Project, Skill, ContactMessage
from .serializers import (
    ProfileSerializer, 
    CompanySerializer, 
    ExperienceSerializer, 
    ProjectSerializer, 
    SkillSerializer,
    ContactMessageSerializer
)

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

from django.core.mail import send_mail
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
            send_mail(
                subject,
                content,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            # We still return success because it's saved in DB
            print(f"Email failed to send: {e}")
