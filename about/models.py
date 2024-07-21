from django.db import models

# Create your models here.

class FAQs(models.Model):
    class Meta:
        verbose_name_plural = 'FAQs'

    question = models.CharField(max_length=100, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.question


class Newsletter(models.Model):
    class Meta:
        verbose_name_plural = 'Newsletter list'

    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email
