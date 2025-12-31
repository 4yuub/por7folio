from django.db import models
from image_cropping import ImageRatioField

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', blank=True)
    cropping = ImageRatioField('profile_picture', '400x400')

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='companies/', blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['order', '-id']

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.ForeignKey(Company, related_name='experiences', on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date', 'order']

    def __str__(self):
        return f"{self.role} at {self.company.name}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    cropping = ImageRatioField('image', '800x450')
    url = models.URLField(blank=True, verbose_name="Deployed URL")
    github_url = models.URLField(blank=True, verbose_name="GitHub URL")
    technologies = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"Image for {self.project.title}"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('DevOps', 'DevOps'),
        ('Data/AI', 'Data/AI'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
