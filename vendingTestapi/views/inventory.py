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

    def list(self, request):
        inventory = Inventory.objects.all()

        serializer = InventorySerializer(inventory, many=True, context={'request': request})

        inv_remainging = []
        for data in serializer.data:
            inv_remainging.append(data['quantity'])

        return Response(inv_remainging, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        inventory = Inventory.objects.get(pk=pk)

        serializer = InventorySerializer(inventory, context={'request': request})

        return Response(serializer.data["quantity"], status=status.HTTP_200_OK)

    def update(self, request, pk=None):

        inventory = Inventory.objects.get(pk=pk)

        coin = Coin.objects.get(pk=1)

        # inv_serializer = InventorySerializer(inventory, context={'request': request})
        # coin_serializer = CoinSerializer(coin, context={'request': request})

        # inv_price = inv_serializer.data["price"]
        # inv_qty = inv_serializer.data["quantity"]
        # coin_qty = (coin_serializer.data["quantity"])

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
                inv_remaining = inv_qty
                coin_return = coin_qty - inv_price
                coin.quantity = 0
                inventory.save()
                coin.save()
                return Response(status=status.HTTP_200_OK, headers={"X-Coins": coin_return})