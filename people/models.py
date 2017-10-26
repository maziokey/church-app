from django.db import models

# Create your models here.
class Parishioner(models.Model):
    name = models.CharField(max_length=41)
    date_of_birth = models.DateField('date of birth', blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    start_date = models.DateField('date posted')
    societys = models.ManyToManyField(Society, blank=True, related_name='parishoners')
    community = models.ForeignKey(Community, blank=True, related_name='parishoners')
    sacraments = models.ManyToManyField(Sacrament, blank=True, related_name='parishoners')
    slug = models.SlugField(max_length=31, unique=True)

class Society(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    leader = models.CharField(max_length=41)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(max_length=31, unique=True)

class Community(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    leader = models.CharField(max_length=41)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(max_length=31, unique=True)

class Sacrament(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    slug = models.SlugField(max_length=31, unique=True)

class Festival(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    festival_date = models.DateField('festival date')
    colors = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31, unique=True)
