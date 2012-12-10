from main.models import *
from main.serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response

class OneItem(generics.RetrieveUpdateDestroyAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        item_id = kwargs['id']
        try:
            one_item = Item.objects.get(id=int(item_id))
        except Item.DoesNotExist:
            data_response = {'error':'Item net found'}
        else:
            item_serializer = ItemSerializer(one_item)
            data_response = item_serializer.data 
        return Response(data_response)
