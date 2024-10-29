from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)

def __str__(self):
    return f"{self.name} - {self.email}"