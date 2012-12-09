from rest_framework import serializers
from main.models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    item_id = serializers.Field(source='id')
    item_type = serializers.Field(source='item_type.name')

    class Meta:
        model = Item
        fields = ('item_id', 'name', 'description', 'updated', 'item_type')
