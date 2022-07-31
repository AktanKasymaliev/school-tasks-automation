from django.urls import path

from school.views import HomeView
from school.views import DeleteStudentView
from school.views import StudentCreateView
from school.views import StudentRetrieveView
from school.views import ConfirmDeleteView
from school.views import UpdateStudentView
from school.views import AllStudentsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('all-students/', AllStudentsView.as_view(), name='all_students'),
    path('student-add/', StudentCreateView.as_view(), name='student_add'),
    path('student/<int:pk>/', StudentRetrieveView.as_view(), name='student'),
    path('student-update/<int:pk>/', UpdateStudentView.as_view(), name='student_update'),
    path('confirm-delete/<int:pk>/', ConfirmDeleteView.as_view(), name='confirm_delete'),
    path('student-delete/<int:pk>/', DeleteStudentView.as_view(), name='student_delete')
]