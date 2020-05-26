from django.db import models
from django.utils import timezone


from accounts.models import CustomUser

class Menu(models.Model):

    title = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='food/%Y/%m/%d/')
    price = models.CharField(max_length=12)
    is_available = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title