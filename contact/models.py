from django.db import models

# Create your models here.

class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Customer messages'

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.name