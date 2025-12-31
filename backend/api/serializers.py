from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer
from .models import Profile, Company, Experience, Project, Skill, ContactMessage, ProjectImage

class ProfileSerializer(serializers.ModelSerializer):
    cropped_picture = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'

    def get_cropped_picture(self, obj):
        if obj.profile_picture and obj.cropping:
            thumbnail_options = {'size': (400, 400), 'crop': True, 'box': obj.cropping}
            url = get_thumbnailer(obj.profile_picture).get_thumbnail(thumbnail_options).url
            return url
        return None

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'website', 'logo', 'order', 'experiences')

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'image', 'order')

class ProjectSerializer(serializers.ModelSerializer):
    cropped_image = serializers.SerializerMethodField()
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def get_cropped_image(self, obj):
        if obj.image and obj.cropping:
            thumbnail_options = {'size': (800, 450), 'crop': True, 'box': obj.cropping}
            url = get_thumbnailer(obj.image).get_thumbnail(thumbnail_options).url
            return url
        return None

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
