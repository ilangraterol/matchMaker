from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Profile, Interest

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles_list.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'

class InterestListView(ListView):
    model = Interest
    template_name = 'interests_list.html'
    context_object_name = 'interests'

class InterestDetailView(DetailView):
    model = Interest
    template_name = 'interest_detail.html'
    context_object_name = 'interest'

class HomeView(TemplateView):
    template_name = 'index.html'    
