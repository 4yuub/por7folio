from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline
from image_cropping import ImageCroppingMixin
from .models import Profile, Company, Experience, Project, Skill, ContactMessage, ProjectImage

class ExperienceInline(StackedInline):
    model = Experience
    extra = 1

class ProjectImageInline(StackedInline):
    model = ProjectImage
    extra = 3

@admin.register(Profile)
class ProfileAdmin(ImageCroppingMixin, ModelAdmin):
    list_display = ('name', 'title', 'email')

@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = ('name', 'location', 'order')
    list_editable = ('order',)
    inlines = [ExperienceInline]

@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'is_current', 'order')
    list_editable = ('is_current', 'order')
    list_filter = ('company', 'is_current')

@admin.register(Project)
class ProjectAdmin(ImageCroppingMixin, ModelAdmin):
    list_display = ('title', 'technologies', 'order')
    list_editable = ('order',)
    inlines = [ProjectImageInline]

@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject')
