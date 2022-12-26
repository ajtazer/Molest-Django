from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    foto = models.FileField(upload_to='foto')
    email = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    more_service = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name.upper()
    