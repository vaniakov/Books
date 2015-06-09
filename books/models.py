from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name="e-mail")

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class LutsManager(models.Manager):
    def get_query_set(self):
        return super(LutsManager, self).get_query_set().filter(author = 'Mark Luts')

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True )
    #                                   ("e-mail", blank=True)
    num_pages = models.IntegerField(blank=True, null=True)
    # objects = BookManager()
    objects = models.Manager()
    luts_objects = LutsManager()

    def __unicode__(self):
        return self.title
