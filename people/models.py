from django.db import models
from django.core.urlresolvers import reverse

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

    def get_absolute_url(self):
        return reverse('people_society_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('people_society_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('people_society_delete', kwargs={'slug': self.slug})

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

    def get_absolute_url(self):
        return reverse('people_community_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('people_community_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('people_community_delete', kwargs={'slug': self.slug})

    class meta:
        ordering = ['name']
        verbose_name_plural = "communities"

class Sacrament(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField()
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people_sacrament_detail', kwargs={'slug': self.slug})

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

    def get_absolute_url(self):
        return reverse('people_festival_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('people_festival_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('people_festival_delete', kwargs={'slug': self.slug})

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
    community = models.ForeignKey(Community, blank=True, related_name='parishoners')
    sacraments = models.ManyToManyField(Sacrament, blank=True, related_name='parishoners')
    slug = models.SlugField(max_length=31, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('people_parishioner_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('people_parishioner_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('people_parishioner_delete', kwargs={'slug': self.slug})

    class meta:
        ordering = ['name']
        verbose_name_plural = "parishioners"
