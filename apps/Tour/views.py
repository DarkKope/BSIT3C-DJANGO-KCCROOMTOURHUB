from django.shortcuts import render, get_object_or_404
from .models import Classroom, Tour, TourScene, SchoolInfo

def landing_page(request):
    return render(request, 'landing.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def rooms_page(request):
    classrooms = Classroom.objects.filter(status='published')
    return render(request, 'rooms.html', {'classrooms': classrooms})

def about_page(request):
    school_info = SchoolInfo.objects.first()
    return render(request, 'about.html', {'school_info': school_info})

def view_room(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id, is_published=True)
    scene = tour.scenes.first() 
    
    all_scenes = TourScene.objects.filter(tour__is_published=True).select_related('tour__classroom')
    
    return render(request, 'tour_view.html', {
        'tour': tour, 
        'scene': scene,
        'all_scenes': all_scenes
    })