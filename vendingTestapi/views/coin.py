from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingTestapi.models import Coin


class CoinSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Coin
        url = serializers.HyperlinkedIdentityField(
            view_name='coin',
            lookup_field='id'
        )
        fields = ('id', 'quantity')

class Coins(ViewSet):

    def list(self, request):
        coin = Coin.objects.all()

        serializer = CoinSerializer(coin, many=True, context={'request': request})

        return Response(serializer.data)

#this function takes the put HTTP request and adds the number of coins in the request body and saves it to the current coin total in the database. It also returns the total amount in the database a a response in the headers
    def put(self, request):

        coin = Coin.objects.get(pk=1)

        coin.quantity = coin.quantity + request.data["coin"]
        coin.save()

        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Coins': coin.quantity})

#this function takes the delete HTTP request, determines how many coins are available, and then return the # of coins back to user and then sets the total back to 0 and updates the database
    def delete(self, request):

        coin = Coin.objects.get(pk=1)
        returned = coin.quantity
        coin.quantity = 0
        coin.save()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Coins': returned})