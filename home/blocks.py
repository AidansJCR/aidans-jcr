from wagtail.core import blocks


class LinkedButtonBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    url = blocks.URLBlock()
    #Could add hex colour codes + image selection in the future

    class Meta():
        template = "home/blocks/LinkedButtonBlock.html"


class SectionBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    colour = blocks.CharBlock(required=False)
    body = blocks.RichTextBlock()

    class Meta():
        template = "home/blocks/SectionBlock.html"
