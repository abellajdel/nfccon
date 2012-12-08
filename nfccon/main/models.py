from django.db import models


class ItemType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
         return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    item_type = models.ForeignKey(ItemType)

    def __unicode__(self):
         return self.name


class NfcTag(models.Model):
    item = models.ForeignKey(Item)    

    def __unicode__(self):
        return 'tag for item: %s' % self.item
