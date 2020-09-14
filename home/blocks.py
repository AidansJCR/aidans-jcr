from wagtail.core.blocks import CharBlock, URLBlock, RichTextBlock, TextBlock, PageChooserBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock


class LinkedButtonBlock(StructBlock):
    name = CharBlock()
    url = URLBlock()
    #Could add hex colour codes + image selection in the future

    class Meta():
        template = "home/blocks/LinkedButtonBlock.html"


class SectionBlock(StructBlock):
    title = CharBlock()
    colour = CharBlock(required=False)
    body = RichTextBlock()

    class Meta():
        template = "home/blocks/SectionBlock.html"


class LinkBlock(StructBlock):
    name = CharBlock(max_length=100)
    description = TextBlock()
    image = ImageChooserBlock()
    destination_page =  PageChooserBlock()

    class Meta():
        template = "home/blocks/LinkBlock.html"
