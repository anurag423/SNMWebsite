from django.db import models

# Create your models here.
class restaurant(models.Model):
    name=models.CharField(max_length=64, help_text='Name of Restaurant')
    city=models.ManyToManyField(max_length=64, help_text='City of Restaurant')
    state=models.ManyToManyField(max_length=64, help_text='State of Restaurant')
    country=models.ManyToManyField(max_length=64, help_text='Country of Restaurant')
    zipcode=models.CharField(max_length=10, help_text='Zip Code of Restaurant')
    ph=models.CharField(max_length=10, help_text='Phone Number of Restaurant')
    website=models.CharField(max_length=200, help_text='Website of Restaurant')
    class Meta:
        ordering = ['name']
    def _str_(self):
        return self.name

