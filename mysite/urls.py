from django.contrib import admin
from django.urls import path, include
from apps.Tour import views as tour_views

urlpatterns = [
    # 1. The Django Admin Panel
    path('admin/', admin.site.urls),

    # 2. The Public ClassroomTourHub Homepage
    path('', tour_views.dashboard, name='dashboard'),

    # 3. The 360 Room Viewer
    path('tour/<int:tour_id>/', tour_views.view_room, name='view_room'),

    # 4. Your old ProjectV3 users app
    path('users/', include('apps.users.urls')), 
]