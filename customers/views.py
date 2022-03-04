from django.views.generic import ListView

from .models import Customer


class CustomersListView(ListView):
    model = Customer
    context_object_name = 'Customers'
    template_name = 'pages/ourcustomers.html'
    page_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super(CustomersListView, self).get_context_data(**kwargs)

        context['customers'] = Customer.objects.filter(status=Customer.STATUS_IS_PUBLISHED)

        return context
