from django.db import models
from django.conf import settings
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Collection
from wagtail.wagtailcore.models import Page, Orderable

# Create your models here.

class Album(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200, blank=True)
