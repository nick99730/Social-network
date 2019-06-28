from django.db import models
from django.urls import reverse


class Person(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=6, choices=SEX, null=True)
    date_of_birth = models.DateField(max_length=8)
    current_city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', default='images/default_ava.png')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Persons"
        ordering = ["last_name", "first_name"]

# Create your models here.
