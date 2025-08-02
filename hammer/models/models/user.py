from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import string


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    invite_code = models.CharField(max_length=6, null=False, blank=False)
    used_invite_code = models.CharField(max_length=6, null=True, blank=False)

    def save(self, *args, **kwargs):
           if not self.invite_code:
               self.invite_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
               self.username = self.phone_number
           super().save(*args, **kwargs)
    class Meta:
        db_table = "users"
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"
