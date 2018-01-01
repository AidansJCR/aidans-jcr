from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.contrib.modeladmin.views import CreateView, EditView
from .models import Transaction

class CreateTransactionView(CreateView):
    exclude = ('creator',)
    def save_model(self, request, obj, form, change):
        """ Extend the save model to store the user who initiated the transaction """
        print("Create Transaction View")
        obj.creator = request.user
        super(CreateTransactionView, self).save_model(request, obj, form, change)

class EditTransactionView(EditView):
    pass



class TransactionModelAdmin(ModelAdmin):
    model = Transaction
    menu_label = 'Transactions'  # ditch this to use verbose_name_plural from model
    menu_icon = 'date'  # change as required
    menu_order = 500 # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = True # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', 'created_at', 'money_to_pay', 'creator', 'debtor')
    list_filter = ('name', 'created_at', 'money_to_pay')
    search_fields = ('name')
    exclude = ('creator',)

    # now define custom views:
    create_view_class = CreateTransactionView
    edit_view_class = EditTransactionView

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(TransactionModelAdmin)
