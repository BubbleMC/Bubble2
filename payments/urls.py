from django.urls import path

from payments.views import PaymentView


urlpatterns = [
    path('success/', PaymentView.as_view()),
    path('fail/', PaymentView.as_view()),


    path('<str:aggregator>/handler/<int:number>/', PaymentView.as_view(), name='payment_handler'),
    path('<str:aggregator>/handler/', PaymentView.as_view(), name='payment_single_handler'),

    path('<str:aggregator>/redirect/<int:number>/', PaymentView.as_view(redirect=True), name='payment_redirect'),
    path('<str:aggregator>/redirect/', PaymentView.as_view(redirect=True), name='payment_single_redirect'),
]
