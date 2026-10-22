from django.shortcuts import render, get_object_or_404
from .models import Classroom, Tour

def dashboard(request):
    # Only fetch classrooms where the status is 'published'
    classrooms = Classroom.objects.filter(status='published')
    return render(request, 'dashboard.html', {'classrooms': classrooms})

def view_room(request, tour_id):
    # Only allow viewing tours that are published
    tour = get_object_or_404(Tour, id=tour_id, is_published=True)
    scene = tour.scenes.first() 
    return render(request, 'tour_view.html', {'tour': tour, 'scene': scene})