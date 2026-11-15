from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    VISIBILITY_CHOICES = [('private', 'Private'), ('public', 'Public')]
    STATUS_CHOICES = [('draft', 'Draft'), ('published', 'Published')]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    grade_level = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tour(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='tours')
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TourScene(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='scenes')
    title = models.CharField(max_length=200)
    
    # THIS IS THE NEW FIELD FOR THE POPUP
    description = models.TextField(blank=True, null=True, help_text="This text will appear as a popup inside the 3D room.")
    
    image_file = models.ImageField(upload_to='scenes/', max_length=255, blank=True, null=True)
    model_file = models.FileField(upload_to='models/', max_length=255, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TourProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    last_viewed_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

class SchoolInfo(models.Model):
    title = models.CharField(max_length=200, default="About Kabankalan Catholic College")
    content = models.TextField(help_text="Enter the mission, vision, and history here.")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title