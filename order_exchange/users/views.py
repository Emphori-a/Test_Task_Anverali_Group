from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from .forms import UserProfileForm
from orders.models import Order

USER = get_user_model()


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = USER
    form_class = UserProfileForm
    template_name = 'registration/user.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy(
            'users:user_profile',
            kwargs={'username': self.request.user.username}
        )


class UserProfileDetailView(LoginRequiredMixin, ListView):
    template_name = 'registration/profile.html'

    def get_user(self):
        return get_object_or_404(USER, username=self.kwargs['username'])

    def get_queryset(self):
        user = self.get_user()
        if user.is_customer:
            return Order.objects.filter(customer=user)
        return Order.objects.filter(executor=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_user()
        return context
