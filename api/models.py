from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class StandardMetadata(models.Model):
    """
    A basic (abstract) model for metadata.
    Subclass new models from 'StandardMetadata' instead of 'models.Model'.
    """
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Recipe(StandardMetadata):
    """Class represents a recipe"""
    name = models.CharField('Name', max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True, max_length=50, help_text="Leave field empty for automatic creation")
    introduction = models.TextField('Introduction', blank=True)
    instructions = models.TextField('Instructions', blank=True)
    preparation_time = models.PositiveSmallIntegerField('Preparation time')
    cooking_time = models.PositiveSmallIntegerField('Cooking time')
    recipe_yield = models.PositiveSmallIntegerField('Yield')
    rating = models.DecimalField('rating', max_digits=2, decimal_places=1)
    #image = FilerImageField(null=True, blank=True, related_name="recipe_image")
    
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    @models.permalink
    def get_absolute_url(self):
        return ('RecipeDetails', [self.slug])

    #def get_image_absolute_url(self):
    #    return self.image.url if self.image else None

    #def get_ingredients(self):
    #    return Ingredient.objects.get(recipe=self)