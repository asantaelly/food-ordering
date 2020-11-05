from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
     Database Table Manager for users table, to create and store user data
    """
    def _create_user(self, email=None, password=None, is_superuser=False, is_staff=False, is_active=False):
        
        if email is None:
            raise ValueError("Email is required")
        if password is None:
            raise ValueError("Password is required")

        user = self.model(
            email = self.normalize_email(email),
            is_superuser = is_superuser,
            is_staff = is_staff,
            is_active = is_active,
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **custom_fields):
        user = self._create_user(email, password, is_active=False, is_staff=False, is_superuser=False)
        user.first_name = custom_fields['first_name']
        user.last_name = custom_fields['last_name']
        user.role = custom_fields['role']
        user.save()
        return user

    def create_superuser(self, email, password, **custom_fields):
        user = self._create_user(email, password, is_superuser=True, is_staff=True, is_active=True)
        user.save()
        return user

