from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from .forms import OrderForm
from .models import Order


class OrderIndexListView(ListView):
    paginate_by = 10
    template_name = 'order_exchange/index.html'
    queryset = Order.objects.all()


@method_decorator(user_passes_test(lambda u: u.is_authenticated
                                   and u.is_customer), name='dispatch')
class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_exchange/order_create.html'

    def get_success_url(self):
        return reverse_lazy(
            'users:user_profile',
            kwargs={'username': self.request.user.username}
        )

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)


class OrderDetailView(DetailView):
    template_name = 'order_exchange/order_detail.html'
    queryset = Order.objects.all()
    pk_url_kwarg = 'order_id'


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_exchange/order_update.html'
    pk_url_kwarg = 'order_id'

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        if order.customer != self.request.user:
            return redirect('orders:order_detail', order_id=order.pk)
        return super().dispatch(request, *args, **kwargs)


class AcceptOrderView(UpdateView):
    model = Order
    pk_url_kwarg = 'order_id'
    fields = []

    def get_success_url(self):
        return reverse_lazy(
            'users:user_profile',
            kwargs={'username': self.request.user.username}
        )

    def form_valid(self, form):
        form.instance.executor = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        if order.executor is None and self.request.user.is_executor:
            return super().dispatch(request, *args, **kwargs)
        return redirect('orders:order_detail', order_id=order.pk)


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_exchange/order_delete.html'
    pk_url_kwarg = 'order_id'
    success_url = reverse_lazy('orders:index')

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        if order.customer != self.request.user:
            return redirect('orders:order_detail', order_id=order.pk)
        return super().dispatch(request, *args, **kwargs)
