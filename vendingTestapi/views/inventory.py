from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingTestapi.models import Inventory
from vendingTestapi.models import Coin


class InventorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Inventory
        url = serializers.HyperlinkedIdentityField(
            view_name='inventory',
            lookup_field='id'
        )
        fields = ('id', 'name', 'quantity', 'price')

class Inventories(ViewSet):

    def list(self, request):
        # inventory = Inventory.objects.getall()

        # serializer = DepartmentSerializer(inventory, many=True, context={'request': request})

        return HttpResponse('Get Method')


    def update(self, request, pk=None):
        inventory = Inventory.objects.get(pk=pk)
        print(inventory)