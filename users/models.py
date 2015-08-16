from django.db import models
from django.core.validators import MinValueValidator

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

#URL
#RANKING

    class Meta:
        ordering = ('created',)
