from django.urls.conf import path

from app.views import all_orders, update_order_state


urlpatterns = [
    path('', all_orders, name='all-orders'),
    path('<int:pk>/update_order_state/', update_order_state, name='update-order-state')
]