from django.db import models
from django.contrib.auth import get_user_model

Teacher = get_user_model()

SEX = (
    ("Male", "Male"),
    ("Female", "Female")
)

class School(models.Model):
    """ School model """
    title = models.CharField(verbose_name="School name", max_length=255)
    grades = models.ManyToManyField("Grade", related_name="school", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'schools'
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

class Student(models.Model):
    """ Student model """
    full_name = models.CharField(verbose_name="Full name", max_length=255)
    email = models.EmailField(verbose_name="Email", unique=True)
    date_of_birth = models.DateField(verbose_name="Date of birth")
    address = models.CharField(verbose_name="Address", max_length=255)
    sex = models.CharField(verbose_name="Sex", max_length=10, choices=SEX)
    school = models.ForeignKey(School, on_delete=models.CASCADE, 
            related_name='student_school')
    grade = models.ForeignKey("Grade", on_delete=models.SET_NULL,
            null=True, blank=True,
            related_name="student_grade")

    def __str__(self) -> str:
        return f"Grade: {self.grade} Name: {self.full_name}"

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Grade(models.Model):
    """ Grade model """
    grade = models.CharField(verbose_name="Grade", max_length=4, help_text="11-A")
    teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL,
            null=True, blank=True,
            related_name="teacher_grade")
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name="school_grade")
    
    def __str__(self) -> str:
        return self.grade

    class Meta:
        db_table = 'grades'
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'