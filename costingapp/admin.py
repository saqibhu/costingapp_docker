from django.contrib import admin

from costingapp.models import TblProduct
from costingapp.models import TblPrice
from costingapp.models import TblPriceType
from costingapp.models import TblStatus

admin.site.register(TblProduct)
admin.site.register(TblPrice)
admin.site.register(TblPriceType)
admin.site.register(TblStatus)
