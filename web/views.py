from django.shortcuts import render
from .models import Profile
from .models import Visitor


def home(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'web/home.html', context)

def home(request):
    # Assuming the homepage is tracked with the URL '/'
    visitor = Visitor.objects.get(url='/')
    return render(request, 'web/home.html', {'visitor_count': visitor.visit_count})

