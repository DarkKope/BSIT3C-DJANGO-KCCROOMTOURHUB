from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Classroom, Tour, TourScene, TourProgress, SchoolInfo

admin.site.site_header = "KCC Admin Portal"
admin.site.site_title = "KCC Admin"
admin.site.index_title = "Management Dashboard"

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'status', 'updated_at')
    actions = None # Removes Action Bar

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'is_published', 'updated_at')
    actions = None # Removes Action Bar

@admin.register(TourScene)
class TourSceneAdmin(admin.ModelAdmin):
    list_display = ('title', 'tour', 'created_at')
    actions = None # Removes Action Bar
    fieldsets = (
        ('Scene Information', {'fields': ('tour', 'title', 'description')}),
        ('3D / Image Upload', {'fields': ('image_file', 'model_file')}),
    )

@admin.register(TourProgress)
class TourProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'last_viewed_at', 'completed')
    actions = None # Removes Action Bar

@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    actions = None # Removes Action Bar