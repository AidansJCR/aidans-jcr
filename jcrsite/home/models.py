from __future__ import absolute_import, unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class HomePage(Page):
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery Images"),  # the carousel on the page
        InlinePanel('main_cards', label="Card Views")
    ]


class MainPageStaticCard(Orderable):
    page = ParentalKey(HomePage, related_name="main_cards")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    card_title = models.CharField(blank=True, max_length=250)
    label = RichTextField(blank=True)
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('card_title'),
        FieldPanel('label'),
    ]


class MainPageCarouselImage(Orderable):
    page = ParentalKey(HomePage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    title = models.CharField(blank=True, max_length=250)
    description = models.CharField(blank=True, max_length=500)
    primary = models.BooleanField(default=False)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('primary'),
    ]
