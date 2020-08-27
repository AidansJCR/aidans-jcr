from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtailmenus.models import MenuPage
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)


class Item(models.Model):
    name = models.CharField(max_length=200)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = RichTextField(null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name="+", null=True, blank=True
    )

    class Meta():
        abstract = True


class Toastie(Item):
    #These will be basically presets and inherit the attributes of item and a set of ingredients
    #The price of this and any allergens can be found using the set of ingredients
    ingredients = models.JSONField()


class Ingredient(Item):
    #This will inherit the attributes of item as well as any allergens (the toastie class can alert the user of these)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = StreamField([
    ('category', blocks.ChoiceBlock(choices=['bread', 'cheese', 'meat', 'other', 'sauce']))
    ])
    allergens = StreamField([
    ('category', blocks.ChoiceBlock(choices=['dairy', 'eggs', 'meat', 'nuts']))
    ])
