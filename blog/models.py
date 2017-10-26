from django.db import models

# Create your models here.
class Sermon(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date')

class Issue(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date')

class Announcement(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date')

class Project(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    members = models.TextField()
    start_date = models.DateField('start date', auto_now_add=True)
    ONGOING = 'ON'
    COMPLETED = 'CPT'
    PROJECT_CHOICES = ((ONGOING, 'ongoing'), (COMPLETED, 'completed'),)
    status = models.CharField(
        max_length=2,
        choices=PROJECT_CHOICES,
        default=ONGOING,
    )
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='start_date')
