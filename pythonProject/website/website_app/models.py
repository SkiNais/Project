from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class SiteImage(models.Model):
    title = models.CharField("Название", max_length=100)
    image = models.ImageField("Изображение", upload_to="site_images/")
    alt_text = models.CharField("Alt-текст", max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title