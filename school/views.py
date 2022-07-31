from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from school.forms import StudentCreateForm
from school.forms import StudentUpdateForm
from school.models import Student

class HomeView(generic.View):

    def get(self, request):
        return render(
            request,
            'pages/home.html'
        )

class StudentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "pages/student_add.html"
    form_class = StudentCreateForm
    model = Student

    def get_success_url(self) -> str:
        return reverse('home')

class StudentRetrieveView(LoginRequiredMixin, generic.DetailView):
    template_name = 'pages/student_detail.html'
    model = Student
    queryset = Student.objects.prefetch_related('school')

class ConfirmDeleteView(LoginRequiredMixin, generic.View):
    
    def get(self, request, pk):
        return render(
            request, 
            "pages/student_confirm_delete.html",
            {"pk": pk}
        )

class DeleteStudentView(LoginRequiredMixin, generic.View):

    def get(self, request, pk):
        query = Student.objects.get(pk=pk)
        query.delete()
        return redirect('home')

class UpdateStudentView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'pages/student_update.html'
    model = Student
    queryset = Student.objects.prefetch_related('school')
    form_class = StudentUpdateForm

    def get_success_url(self) -> str:
        return reverse('home')

class AllStudentsView(LoginRequiredMixin, generic.ListView):
    model = Student
    template_name = 'pages/students_list.html'

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query is None:
            student_list = Student.objects.prefetch_related('school')
        else:
            student_list = Student.objects.filter(
                Q(full_name__icontains=query) | Q(school__title__icontains=query)
            )
        return student_list

#TODO MAIL(SIGNALS), MAILING