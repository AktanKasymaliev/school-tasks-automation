from django.db import models
from django.contrib.auth.models import  PermissionsMixin, AbstractBaseUser

from teachers.manager import TeacherManager

class Teacher(AbstractBaseUser, PermissionsMixin):

    full_name =  models.CharField(verbose_name='Full name', max_length=255, help_text='Niazalieva Zarema Abdurasulovna')
    phone_number = models.CharField(verbose_name="Phone number", max_length=11, unique=True, help_text='0555055934')
    subject = models.CharField(verbose_name='Subject name', max_length=25, help_text='World history')
    created_at = models.DateField(verbose_name="Date of creation", auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = TeacherManager()

    def __str__(self) -> str:
        return f'Teacher: {self.full_name}'

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'