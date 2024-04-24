from django.urls import include, path

from .views import (AcceptOrderView, OrderCreateView, OrderDeleteView,
                    OrderDetailView, OrderIndexListView, OrderUpdateView)

app_name = 'orders'

order_urls = [
    path('create/', OrderCreateView.as_view(), name='create_order'),
    path('<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('accept/<int:order_id>/', AcceptOrderView.as_view(),
         name='accept_order'),
    path('edit/<int:order_id>/', OrderUpdateView.as_view(), name='edit_order'),
    path('delete/<int:order_id>/', OrderDeleteView.as_view(),
         name='delete_order')
]

urlpatterns = [
    path('', OrderIndexListView.as_view(), name='index'),
    path('orders/', include(order_urls)),
]
