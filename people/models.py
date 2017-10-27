from django.db import models

# Create your models here.
class Society(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    leader = models.CharField(max_length=41)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name_plural = "societies"

class Community(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    leader = models.CharField(max_length=41)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name_plural = "communities"

class Sacrament(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name_plural = "sacraments"

class Festival(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    festival_date = models.DateField('festival date')
    colors = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name_plural = "festivals"

class Parishioner(models.Model):
    name = models.CharField(max_length=41)
    date_of_birth = models.DateField('date of birth', blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    start_date = models.DateField('date posted')
    societies = models.ManyToManyField(Society, blank=True, related_name='parishoners')
    communities = models.ForeignKey(Community, blank=True, related_name='parishoners')
    sacraments = models.ManyToManyField(Sacrament, blank=True, related_name='parishoners')
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']
        verbose_name_plural = "parishoners"
