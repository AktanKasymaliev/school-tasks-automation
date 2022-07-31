from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import  get_user_model
from django.contrib import messages

from teachers.forms import LogInForm, SignUpForm

Teacher = get_user_model()

class SignUpView(generic.CreateView):
    template_name = 'auth/signup.html'
    model = Teacher
    form_class = SignUpForm

    def get_success_url(self) -> str:
        return reverse('home')

class LogInView(generic.FormView):
    template_name = 'auth/login.html'
    form_class = LogInForm

    def post(self, request: HttpRequest):
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        teacher = authenticate(request, 
                phone_number=phone_number,
                password=password
            )
            
        if not teacher:
            print("Credentials are not correct!")

        login(request, teacher)
        return redirect('home')

class LogOutView(generic.View):
    
    def get(self, request):
        logout(request)
        # messages.add_message(request, messages.SUCCESS, "Logout successfully")
        return redirect('home')