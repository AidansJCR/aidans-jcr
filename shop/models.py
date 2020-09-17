from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtailmenus.models import MenuPage
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from multiselectfield import MultiSelectField


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='shop_images')

    class Meta():
        abstract = True


class Ingredient(Item):
    #This will inherit the attributes of item as well as any allergens (the toastie class can alert the user of these)
    category = [('b', 'bread'), ('c', 'cheese'), ('m', 'meat'), ('o', 'other'), ('s', 'sauce')]
    allergen_options = [('d', 'dairy'), ('e', 'eggs'), ('m', 'meat'), ('n', 'nuts')]
    allergens = MultiSelectField(choices=allergen_options)


class Toastie(Item):
    #These will be basically presets and inherit the attributes of item and a set of ingredients
    #The price of this and any allergens can be found using the set of ingredients
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
