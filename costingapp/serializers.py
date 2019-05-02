from rest_framework import serializers
from .models import TblProduct, TblPrice, TblStatus


class TblPriceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('tblpricetype', 'price_value')
        model = TblPrice


class TblProductSerializer(serializers.ModelSerializer):
    tblprice = TblPriceSerializer(many=True, required=False)
    # tblstatus = TblStatusSerializer(required=False)

    class Meta:
        fields = (
            'id',
            'isbn13',
            'impression',
            'full_title',
            'tblstatus',
            'tblprice'
        )
        model = TblProduct

    def create(self, validated_data):
        tblprice_data = validated_data.pop('tblprice')
        tblproduct = TblProduct.objects.create(**validated_data)
        for price in tblprice_data:
            TblPrice.objects.create(tblproduct=tblproduct, **price)
        return tblproduct

    def update(self, instance, validated_data):
        # other updateable fields
        instance.full_title = validated_data.get(
            'full_title', instance.full_title)
        instance.tblstatus = validated_data.get(
            'tblstatus', instance.tblstatus)
        instance.save()
        # end other updateable fields

        # price bit, tricky as it's nested and many=True so just update the whole block
        tblprice_data = validated_data.pop('tblprice')
        tblprice_orig = (instance.tblprice).all()

        tblprice_orig = list(tblprice_orig)

        for price_data in tblprice_data:
            price = tblprice_orig.pop(0)

            # only update the price where the price type is the same
            price.tblpricetype = price_data.get(
                'tblpricetype', price.tblpricetype)
            price.price_value = price_data.get(
                'price_value', price.price_value)
            price.save()
        # end price bit
        return instance
