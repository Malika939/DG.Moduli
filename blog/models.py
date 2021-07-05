from django.db import models
from django.db.models.fields import DateTimeField


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__ (self):
        return f'{self.title}'