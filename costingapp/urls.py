from django.urls import path

from .views import ListTblProduct, DetailTblProduct

urlpatterns = [
    path('tblproduct/', ListTblProduct.as_view()),
    path('tblproduct/<int:pk>/', DetailTblProduct.as_view()),
]
