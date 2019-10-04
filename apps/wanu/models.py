from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    shot = models.ImageField(upload_to="projects")
    url  = models.URLField(unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created",]

    def __str__(self):
        return self.name