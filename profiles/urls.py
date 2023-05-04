from django.urls import path
from .views import ProfileListView, ProfileDetailView, InterestListView, InterestDetailView, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('interests/', InterestListView.as_view(), name='interest-list'),
    path('interests/<int:pk>/', InterestDetailView.as_view(), name='interest-detail'),
]
