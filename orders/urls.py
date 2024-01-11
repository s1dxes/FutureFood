from django.urls import path
from orders.views import OrderCreateView, CanceledTemplateView, SuccessTemplateView


app_name = 'orders'
urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-canceled/', CanceledTemplateView.as_view(), name='order_canceled'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
]