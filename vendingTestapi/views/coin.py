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

    def update(self, request, pk=None):
        #can't get a put request to be recognized
        coin = Coin.objects.get(pk=1)
        print(request.data)
        # coin.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        coin = Coin.objects.get(pk=pk)
        if coin.quantity > 0:
            return 0
#then set quantity to 0
#send back a response