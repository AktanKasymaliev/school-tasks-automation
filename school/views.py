from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from school.forms import StudentCreateForm
from school.forms import StudentUpdateForm
from school.models import Student

class HomeView(generic.View):

    def get(self, request):
        return render(
            request,
            'pages/home.html'
        )

class StudentCreateView(generic.CreateView):
    template_name = "pages/student_add.html"
    form_class = StudentCreateForm
    model = Student

    def get_success_url(self) -> str:
        return reverse('home')

class StudentRetrieveView(generic.DetailView):
    template_name = 'pages/student_detail.html'
    model = Student
    queryset = Student.objects.prefetch_related('school')

class ConfirmDeleteView(generic.View):
    
    def get(self, request, pk):
        return render(
            request, 
            "pages/student_confirm_delete.html",
            {"pk": pk}
        )

class DeleteStudentView(generic.View):

    def get(self, request, pk):
        query = Student.objects.get(pk=pk)
        query.delete()
        return redirect('home')

class UpdateStudentView(generic.UpdateView):
    template_name = 'pages/student_update.html'
    model = Student
    queryset = Student.objects.prefetch_related('school')
    form_class = StudentUpdateForm

    def get_success_url(self) -> str:
        return reverse('home')

#TODO CRUD, MAIL(SIGNALS), SEARCH, MAILING
# class StudentsModelViewSet()