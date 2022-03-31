from turtle import title
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import ContactForm, OrderForm
from .models import Contact, HomeFeature
from customers.models import Customer, Order, Material


def index(request):
    home_feature = HomeFeature.objects.filter(active=True).last()
    materials = Material.objects.all()
    print(materials)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        logo = request.POST['logo']
        phone = request.POST['phone']
        customer,customer_  = Customer.objects.get_or_create(email = email, name = name, defaults={'logo': logo, 'phone': phone})
        material_type = request.POST['material']
        material,created = Material.objects.get_or_create(title = material_type)
        inner_diameter = request.POST['inner_diameter']
        thickness = request.POST['thickness']
        length = request.POST['length']
        quantity = request.POST['quantity']
        order = Order.objects.create(customer=customer, material = material,
        inner_diameter = inner_diameter, thickness = thickness, length = length,
        quantity=quantity)




    return render(request, 'pages/index.html', {'home_feature': home_feature, 'materials':materials})


class ContactView(CreateView):
    template_name = 'pages/contact.html'
    model = Contact
    form_class = ContactForm
    page_name = 'Contact'
    success_url = reverse_lazy('pages:contact')

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class OurStoryView(TemplateView):
    template_name = "pages/our-story.html"


class SuccessView(TemplateView):
    template_name = "pages/success.html"
