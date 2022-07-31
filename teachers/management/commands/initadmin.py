from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

Teacher = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **options):
        phone_number = "055555555"
        password = "12345678"
        print('Creating account for %s (%s)' % (phone_number, password))
        admin = Teacher.objects.create_superuser(phone_number=phone_number, password=password)
        admin.save()
        print("Test-Admin account created")