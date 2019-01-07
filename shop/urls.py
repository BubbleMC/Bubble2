from django.urls import path

from shop.views import test

urlpatterns = [
    path('category/<slug:name>/', test, name='category')
]
