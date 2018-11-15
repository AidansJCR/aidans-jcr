from django.db import models
from django.conf import settings
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page, Orderable

# Create your models here.

class AlbumPage(Page):
    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        InlinePanel('gallery_images', label="Images"),  # the carousel on the page
    ]
class AlbumImage(Orderable):
    page = ParentalKey(AlbumPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]
