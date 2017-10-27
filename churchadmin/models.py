from django.db import models

# Create your models here.
class Priest(models.Model):
    name = models.CharField(max_length=41)
    mission = models.TextField(help_text='Diocesan or Missionary')
    position = models.CharField(max_length=31, help_text='Your position in the parish')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_posted = models.DateField('date posted')
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name_plural = "priests"

class Sister(models.Model):
    name = models.CharField(max_length=41)
    mission = models.TextField(help_text='Diocesan or Missionary')
    position = models.CharField(max_length=31, help_text='Your position in the parish')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_posted = models.DateField('date posted')
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name_plural = "sisters"

class Cathecist(models.Model):
    name = models.CharField(max_length=41)
    position = models.CharField(max_length=31, help_text='Your position in the parish')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_posted = models.DateField('date posted')
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name_plural = "cathecists"


class AlterBoy(models.Model):
    name = models.CharField(max_length=41)
    start_date = models.DateField('start date')

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name = "alter boys"
