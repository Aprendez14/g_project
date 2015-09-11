from django.db import models
from django.core.validators import MinValueValidator
#probando:
#from model_utils import Choices
from django.template import defaultfilters


class Action(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
#    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=False, default="No description")
    consequence = models.TextField(max_length=300, blank=False)

    class Meta:
        ordering = ('name',)



# Create your models here.
class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    player_type = models.CharField(max_length=100, blank=False, default="Undefined")
    learning_style = models.CharField(max_length=100, blank=False, default="Undefined")

#    PTYPE = (("Undefined", "Undefined"), ("Explorer", "Explorer"), ("Killer", "Killer"), ("Socializer", "Socializer"), ("Achiever", "Achiever"))
#    player_type = models.CharField(choices=PTYPE, max_length=100, default="Undefined")

#    LSTYLE = ((1, "Undefined"), (2, "Activist"), (3, "Reflector"), (4, "Pragmatist"), (5, "Theoretician"))
#    learning_style = models.CharField(choices=LSTYLE, max_length=100, default="Undefined")

    golden_badges = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    silver_badges = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    bronze_badges = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    points = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    percent_in_level = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    #last_login = models.DateTimeField(blank=True)

    class Meta:
        ordering = ('created',)
