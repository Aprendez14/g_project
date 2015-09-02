from django.db import models
from django.core.validators import MinValueValidator
#probando:
from django.template import defaultfilters


#probando:
class Action(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=False, default="No description")
    consequence = models.TextField(max_length=300, blank=False)


    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Action, self).save(*args, **kwargs)

#    def save(self, *args, **kwargs):
#        if not self.id:
#            self.slug = slughifi(self.name)
#        super(Action, self).save(*args, **kwargs)


    class Meta:
        ordering = ('name',)



# Create your models here.
class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    golden_badges = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    silver_badges = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    bronze_badges = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    points = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    level = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    percent_in_level = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    #last_login = models.DateTimeField()
    #id_action = models.ForeignKey(Action)

    class Meta:
        ordering = ('created',)
