from django.urls import path

from payments.views import test


urlpatterns = [
    path('success/', test),
    path('fail/', test),

    path('unitpay/handler/<int:number>', test, name='unitpay_handler'),
    path('unitpay/handler', test, name='unitpay_single_handler'),
    path('free-kassa/handler/<int:number>', test, name='free_kassa_handler'),
    path('free-kassa/handler', test, name='free_kassa_single_handler'),
    path('interkassa/handler/<int:number>', test, name='inter_kassa_handler'),
    path('interkassa/handler', test, name='inter_kassa_single_handler'),

    path('unitpay/redirect/<int:number>', test, name='unitpay_redirect'),
    path('unitpay/redirect', test, name='unitpay_single_redirect'),
    path('free-kassa/redirect/<int:number>', test, name='free_kassa_redirect'),
    path('free-kassa/redirect', test, name='free_kassa_single_redirect'),
    path('interkassa/redirect/<int:number>', test, name='inter_kassa_redirect'),
    path('interkassa/redirect', test, name='inter_kassa_single_redirect'),
]
