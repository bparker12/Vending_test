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

    def put(self, request):

        coin = Coin.objects.get(pk=1)
        print(request.data["coin"])

        coin.quantity = coin.quantity + request.data["coin"]
        coin.save()

        reponse = "X-Coins:"
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Coins': coin.quantity})

    def delete(self, request):

        coin = Coin.objects.get(pk=1)
        returned = coin.quantity
        coin.quantity = 0
        coin.save()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Coins': returned})
#then set quantity to 0
#send back a response