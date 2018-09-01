from wagtail.wagtailcore import blocks

class LinkedButtonBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    url = blocks.URLBlock()
    #Could add hex colour codes + image selection in the future

    class Meta():
        template = "home/blocks/LinkedButtonBlock.html"
