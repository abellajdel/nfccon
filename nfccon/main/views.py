from main.models import *
from main.serializers import *
from rest_framework import generics, permissions
from rest_framework.response import Response

class OneItem(generics.RetrieveUpdateDestroyAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        #Todo (Amine): Enhance the view to return error as json if item not found 
        item_id = kwargs['id']
        one_item = Item.objects.get(id=int(item_id))
        serializer = ItemSerializer(one_item)
        return Response(serializer.data)
