from django.db import models


class TblStatus(models.Model):
    status_desc = models.CharField(max_length=55)

    def __str__(self):
        return self.status_desc


class TblPriceType(models.Model):
    price_type = models.CharField(max_length=55)

    def __str__(self):
        return self.price_type


class TblProduct(models.Model):
    tblstatus = models.ForeignKey(
        TblStatus, related_name='tblproduct', null=True, on_delete=models.CASCADE)
    impression = models.IntegerField(null=True)
    full_title = models.CharField(max_length=55, null=True)
    isbn13 = models.CharField(max_length=13, null=True)

    def __str__(self):
        return '%d: %s' % (self.impression, self.full_title)


class TblPrice(models.Model):
    tblproduct = models.ForeignKey(
        TblProduct, related_name='tblprice', on_delete=models.CASCADE)
    tblpricetype = models.ForeignKey(
        TblPriceType, on_delete=models.CASCADE)
    price_value = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return '%d: %.2f' % (self.tblproduct_id, self.price_value)
