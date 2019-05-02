from django.urls import path

from .views import ListTblProduct, DetailTblProduct

urlpatterns = [
    path('', ListTblProduct.as_view()),
    path('<int:pk>/', DetailTblProduct.as_view()),
]
