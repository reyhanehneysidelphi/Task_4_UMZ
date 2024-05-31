from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11, null=True, blank=True)
    summary = models.TextField()
    skills = models.TextField(help_text='Separate your skills with commas')
    experience = models.TextField()
    education = models.TextField()

    def __str__(self):
        return self.name
