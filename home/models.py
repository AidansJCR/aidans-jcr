from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtailmenus.models import MenuPage
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.documents.blocks import DocumentChooserBlock
from home.blocks import LinkedButtonBlock

class BlogPage(MenuPage):
    # owner can be obtained from the owner attribute (in Page).
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('feed_image'),
    ]
    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]
    parent_page_types = ['home.BlogIndexPage']
    subpage_types = []

    def get_context(self, request):
        context = super(BlogPage, self).get_context(request)

        # Get the full name if it exists, otherwise use the username
        owner_username = self.owner
        user = User.objects.filter(username=owner_username).first()
        context['owner_fullname'] = user.get_full_name()
        return context


class GenericPage(MenuPage):
    subtitle = models.CharField(blank=True, max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]


class HomePage(MenuPage):
    body = RichTextField(blank=True)
    show_blog_posts = models.BooleanField()
    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery Images"),  # the carousel on the page
        InlinePanel('main_cards', label="Card Views"),
        FieldPanel('show_blog_posts')
    ]
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)

        # TODO: Allow the user to customise the number
        # TODO: allow filter by category, such as news tags.
        # Now get the recent blog posts
        blog_posts = BlogPage.objects.live().public()
        blog_posts = blog_posts.order_by('-first_published_at')[:5]
        context['blog_posts'] = blog_posts

        #return the context
        return context

class BlogIndexPage(MenuPage):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    subpage_types = ['home.BlogPage']
    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)

        # Get all the Blog Posts that are made under this index page.
        blog_posts = self.get_children().live().public().type(BlogPage)

        # Send them to the page template as {{ blog_posts }}.
        context['blog_posts'] = blog_posts
        return context

class PeopleDirectoryPage(MenuPage):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        InlinePanel('people')
    ]

class LinkPage(MenuPage):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        InlinePanel('links')
    ]

class ClubPage(MenuPage):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        InlinePanel('club')
    ]

class DocumentPage(MenuPage):
    intro = RichTextField();
    section_blocks = StreamField([
        ('heading', blocks.CharBlock(classname="Section Title")),
        ('document', DocumentChooserBlock())
    ])

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('section_blocks')
    ]



class Club(Orderable):
    page = ParentalKey(ClubPage, related_name='club')
    name = models.CharField(max_length=200)
    description = RichTextField()
    leader = models.CharField(max_length=100)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name="+"
    )
    facebook_link = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)
    twitter_link = models.URLField(blank=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('leader'),
        ImageChooserPanel('image'),
        FieldPanel('facebook_link'),
        FieldPanel('email_address'),
        FieldPanel('twitter_link')
    ]
class PageLinks(Orderable):
    page = ParentalKey(LinkPage, related_name='links')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    destination_page =  models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        ImageChooserPanel('image'),
        PageChooserPanel('destination_page')
    ]
class PersonProfile(Orderable):
    page = ParentalKey(PeopleDirectoryPage, related_name='people')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    rolename = models.CharField(max_length=100)
    description = models.TextField()
    facebook_links = StreamField([
        ('facebook_link', LinkedButtonBlock())
        ], null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('email'),
        ImageChooserPanel('image'),
        FieldPanel('rolename'),
        FieldPanel('description'),
        StreamFieldPanel('facebook_links'),
    ]


class MainPageStaticCard(Orderable):
    page = ParentalKey(HomePage, related_name="main_cards")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    card_title = models.CharField(blank=True, max_length=250)
    label = RichTextField(blank=True)
    destination_page =  models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('card_title'),
        FieldPanel('label'),
        PageChooserPanel('destination_page'),
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


class AppAnnouncement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    time_set = models.TimeField()
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
