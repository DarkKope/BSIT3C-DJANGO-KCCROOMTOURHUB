from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.Tour import views as tour_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tour_views.landing_page, name='landing'),
    path('dashboard/', tour_views.dashboard, name='dashboard'),
    path('rooms/', tour_views.rooms_page, name='rooms'),
    path('about/', tour_views.about_page, name='about'),
    path('tour/<int:tour_id>/', tour_views.view_room, name='view_room'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)