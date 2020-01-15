from django.db import models

# Create your models here.
class Job(models.Model):

    title = models.CharField(blank = True, max_length=100)
    summary = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def ___str___(self):
        return self.summary
