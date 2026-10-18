from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    VISIBILITY_CHOICES = [
        ('private', 'Private'),
        ('unlisted', 'Unlisted'),
        ('public', 'Public'),
    ]
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    # Links to Django's built-in user authentication
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classrooms')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    grade_level = models.CharField(max_length=50, blank=True, null=True)
    cover_image_url = models.URLField(blank=True, null=True)
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='private')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tour(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='tours')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    scene_order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.classroom.name} - {self.title}"

class TourScene(models.Model):
    PANORAMA_TYPES = [
        ('equirectangular', 'Equirectangular'),
        ('cubemap', 'Cubemap'),
        ('flat', 'Flat'),
    ]

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='scenes')
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    panorama_type = models.CharField(max_length=20, choices=PANORAMA_TYPES, default='equirectangular')
    initial_yaw = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    initial_pitch = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    hotspots = models.JSONField(default=list, blank=True) # Stores 3D hotspot data
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tour.title} - {self.title}"

class TourProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    scene = models.ForeignKey(TourScene, on_delete=models.SET_NULL, null=True, blank=True)
    completed = models.BooleanField(default=False)
    last_viewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'tour') # One progress record per user per tour

    def __str__(self):
        return f"{self.user.username} - {self.tour.title}"