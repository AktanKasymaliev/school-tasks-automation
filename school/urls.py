from django.urls import path

from school.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]