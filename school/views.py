from django.shortcuts import render
from django.views import generic

class HomeView(generic.View):

    def get(self, request):
        return render(
            request,
            'pages/home.html'
        )

#TODO CRUD, MAIL(SIGNALS), SEARCH, MAILING
# class StudentsModelViewSet()