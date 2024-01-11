from django.views.generic.edit import CreateView
from orders.forms import OrderForm
from django.urls import reverse_lazy, reverse
from home.models import Basket
from django.conf import settings
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
import stripe
from http import HTTPStatus
stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessTemplateView(TemplateView):
    template_name = 'orders/success.html'
    title = 'FutureFood - thanks for your order'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

class CanceledTemplateView(TemplateView):
    template_name = 'orders/canceled.html'

class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def post(self, request, *args, **kwargs):
        super(OrderCreateView,self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1ORHpWExtQ2inBIKpVYg3udy',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_canceled')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

