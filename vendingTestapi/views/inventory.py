from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingTestapi.models import Inventory
from vendingTestapi.models import Coin
from .coin import CoinSerializer


class InventorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Inventory
        url = serializers.HyperlinkedIdentityField(
            view_name='inventory',
            lookup_field='id'
        )
        fields = ('id', 'name', 'quantity', 'price')

class Inventories(ViewSet):

#this function takes a get request with no id # and then returns an array of the remaining inventories for each item in the inventory
    def list(self, request):
        inventory = Inventory.objects.all()

        serializer = InventorySerializer(inventory, many=True, context={'request': request})

        inv_remainging = []
        for data in serializer.data:
            inv_remainging.append(data['quantity'])

        return Response(inv_remainging, status=status.HTTP_200_OK)

#the retrieve function takes a HTTP request with a id # and then returns the # of items in the inventory for the specific id requested
    def retrieve(self, request, pk=None):

        inventory = Inventory.objects.get(pk=pk)

        serializer = InventorySerializer(inventory, context={'request': request})

        return Response(serializer.data["quantity"], status=status.HTTP_200_OK)


#this function has several features.  it checks to see if there is a sufficent quantity of requested id # to be vended.  If not it returns a 404 code. If there is suffient quantity, it will then check whether there is enough coin inserted to purchase the item based on its price.
    def update(self, request, pk=None):

        inventory = Inventory.objects.get(pk=pk)

        coin = Coin.objects.get(pk=1)

        inv_price = inventory.price
        inv_qty = inventory.quantity
        coin_qty = coin.quantity

        if inv_qty > 0:
            if inv_price > coin_qty:
                coins_short = inv_price - coin_qty
                print(coins_short)
                return Response(status=status.HTTP_403_FORBIDDEN, headers={"X-Coins": coins_short})
            else:
                inventory.quantity = inv_qty - 1
                inv_remaining = inventory.quantity
                vended = {"quantity": 1}

                coin_return = coin_qty - inv_price
                coin.quantity = 0

                inventory.save()
                coin.save()

                headers = {
                    "X-Coins": coin_return,
                    "X-Inventory-Remaining": inv_remaining
                }
                return Response(vended, status=status.HTTP_200_OK, headers=headers)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND, headers={"X-Coins": coin_qty})