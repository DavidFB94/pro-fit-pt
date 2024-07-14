from django.db import models

# Create your models here.

class FAQs(models.Model):
    question = models.CharField(max_length=100, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.question
