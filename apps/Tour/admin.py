from django.contrib import admin
from .models import Classroom, Tour, TourScene, TourProgress

# This creates a nice nested layout in the admin panel
class TourSceneInline(admin.TabularInline):
    model = TourScene
    extra = 1

class TourInline(admin.TabularInline):
    model = Tour
    extra = 1

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'grade_level', 'owner', 'status')
    inlines = [TourInline]

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'is_published', 'created_at')
    inlines = [TourSceneInline]

@admin.register(TourScene)
class TourSceneAdmin(admin.ModelAdmin):
    list_display = ('title', 'tour', 'panorama_type', 'position')

@admin.register(TourProgress)
class TourProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'completed', 'last_viewed_at')