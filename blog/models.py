from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Sermon(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date')

    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog_sermon_detail', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_sermon_update', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog_sermon_delete', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    class meta:
        verbose_name_plural = 'sermons'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

class Issue(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date')

    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog_issue_detail', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_issue_update', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog_issue_delete', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    class meta:
        verbose_name_plural = 'issues'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

class Announcement(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='pub_date')

    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog_announcement_detail', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_announcement_update', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog_announcement_delete', kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

    class meta:
        verbose_name_plural = 'announcements'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

class Project(models.Model):
    title = models.CharField(max_length=63)
    text = models.TextField()
    members = models.TextField()
    start_date = models.DateField('start date', auto_now_add=True)
    ONGOING = 'ON'
    COMPLETED = 'CPT'
    PROJECT_CHOICES = ((ONGOING, 'ongoing'), (COMPLETED, 'completed'),)
    status = models.CharField(
        max_length=5,
        choices=PROJECT_CHOICES,
        default=ONGOING,
    )
    slug = models.SlugField(max_length=63, help_text='A label for URL config', unique_for_month='start_date')

    def __str__(self):
        return "{} on {}".format(self.title, self.start_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog_project_detail', kwargs={'year': self.start_date.year, 'month': self.start_date.month, 'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_project_update', kwargs={'year': self.start_date.year, 'month': self.start_date.month, 'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog_project_delete', kwargs={'year': self.start_date.year, 'month': self.start_date.month, 'slug': self.slug})

    class meta:
        verbose_name_plural = 'projects'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
