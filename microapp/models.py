from django.db import models

# Create your models here.

class contact_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=10, default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file.name