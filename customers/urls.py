from django.urls import re_path

from .views import CustomersListView

app_name = 'customers'
urlpatterns = [
    re_path(r'^$', CustomersListView.as_view(), name='customers_list')
]
