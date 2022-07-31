from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth import  get_user_model

from teachers.forms import LogInForm, SignUpForm
from teachers.funcs import auto_login

Teacher = get_user_model()

class SignUpView(generic.CreateView):
    template_name = 'auth/signup.html'
    model = Teacher
    form_class = SignUpForm

    def post(self, request: HttpRequest):
        result = super().post(request)
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        auto_login(request,
                    phone_number=phone_number, 
                    password=password)
        return result

    def get_success_url(self) -> str:
        return reverse('home')

class LogInView(generic.FormView):
    template_name = 'auth/login.html'
    form_class = LogInForm

    def post(self, request: HttpRequest):
        form = self.get_form()
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        if form.is_valid():
            auto_login(request,
                        phone_number=phone_number, 
                        password=password)
            return redirect('home')
        return render(
            request, self.template_name,
            {"form": form}
        )

class LogOutView(generic.View):
    
    def get(self, request):
        logout(request)
        return redirect('home')