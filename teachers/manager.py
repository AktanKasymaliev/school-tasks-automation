from django.contrib.auth.models import BaseUserManager

class TeacherManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password, *args, **optinal):
        user = self.model(
            phone_number=phone_number,
            **optinal
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, *args, **optinal):
        optinal['is_active'] = True
        optinal['is_staff'] = True
        optinal['is_superuser'] = True
        user = self.create_user(phone_number, password, *args, **optinal)
        return user