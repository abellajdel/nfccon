from django.forms import ModelForm
from datetime import datetime
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'item_type')

    def __init__(self, user=None, **kwargs):
        if user:
            self.user = user
            self.created = datetime.now()
            self.updated = datetime.now()
        super(ItemForm, self).__init__(**kwargs)

    def save(self):
        item = super(ItemForm, self).save(commit=False)
        print "tototototot %s" % item.name
        if not item.pk:
            item.user = self.user
            item.created = self.created
            item.updated = self.updated
        item.save()
        return item
