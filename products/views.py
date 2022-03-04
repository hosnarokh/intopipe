from django.conf import settings
from django.views.generic import ListView, DetailView

from .models import ProductPost, ProductCategory


class PaperTubeListView(ListView):
    model = ProductPost
    context_object_name = 'Paper_Tube'
    template_name = 'pages/paper_tube.html'
    page_name = 'products'

    def get_context_data(self, **kwargs):
        products = ProductPost.objects.filter(category__title=settings.PAPERTUBE,
                                              status=ProductPost.STATUS_IS_PUBLISHED).all()

        context = super(PaperTubeListView, self).get_context_data(**kwargs)

        context['products'] = products
        context['category'] = ProductCategory.objects.filter(title=settings.PAPERTUBE).first()

        return context


class PaperTubeDetailView(DetailView):
    model = ProductPost
    context_object_name = 'Paper_Tube'
    slug_field = 'slug'
    template_name = 'pages/paper_tube_detail.html'
    page_name = 'product'

    def get_context_data(self, **kwargs):
        product = ProductPost.objects.filter(status=ProductPost.STATUS_IS_PUBLISHED, category__title=settings.PAPERTUBE,
                                             slug=self.kwargs.get('slug')).first()
        context = super(PaperTubeDetailView, self).get_context_data(**kwargs)
        context['product'] = product

        return context


class PlasticPipeListView(ListView):
    model = ProductPost
    context_object_name = 'Plastic_Pipe'
    template_name = 'pages/plastic_pipe.html'
    page_name = 'plastic_pipe_list'

    def get_context_data(self, **kwargs):
        products = ProductPost.objects.filter(status=ProductPost.STATUS_IS_PUBLISHED,
                                              category__title=settings.PLASTICPIPE).all()
        context = super(PlasticPipeListView, self).get_context_data(**kwargs)

        context['products'] = products
        context['category'] = ProductCategory.objects.filter(title=settings.PLASTICPIPE).first()

        return context


class PlasticPipeDetailView(DetailView):
    model = ProductPost
    context_object_name = 'product'
    slug_field = 'slug'
    template_name = 'pages/plastic_pipe_detail.html'
    page_name = 'Plastic_Pipe_detail'

    def get_context_data(self, **kwargs):
        product = ProductPost.objects.filter(status=ProductPost.STATUS_IS_PUBLISHED,
                                             category__title=settings.PLASTICPIPE,
                                             slug=self.kwargs.get('slug')).first()
        context = super(PlasticPipeDetailView, self).get_context_data(**kwargs)
        context['product'] = product

        return context


class MetalicPipeListView(ListView):
    model = ProductPost
    context_object_name = 'products'
    template_name = 'pages/metalic_pipe.html'
    page_name = 'metalic_pipe_list'

    def get_context_data(self, **kwargs):
        products = ProductPost.objects.filter(category__title=settings.METALICPIPE,

                                              status=ProductPost.STATUS_IS_PUBLISHED).all()
        context = super(MetalicPipeListView, self).get_context_data(**kwargs)

        context['products'] = products
        context['category'] = ProductCategory.objects.filter(title=settings.METALICPIPE).first()

        return context


class MetalicPipeDetailView(DetailView):
    model = ProductPost
    context_object_name = 'product'
    slug_field = 'slug'
    template_name = 'pages/metalic_pipe_detail.html'
    page_name = 'metalicpipe_detail'

    def get_context_data(self, **kwargs):
        product = ProductPost.objects.filter(status=ProductPost.STATUS_IS_PUBLISHED,
                                             category__title=settings.METALICPIPE,
                                             slug=self.kwargs.get('slug')).first()
        context = super(MetalicPipeDetailView, self).get_context_data(**kwargs)
        context['product'] = product

        return context


class ProductsListView(ListView):
    model = ProductPost
    context_object_name = 'products'
    template_name = 'pages/products.html'
    page_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['products'] = list(ProductPost.objects.filter(status=ProductPost.STATUS_IS_PUBLISHED,
                                                              is_selected=True).all())[-3:]

        return context


class CategoriesListView(ListView):
    model = ProductPost
    context_object_name = 'categories'
    template_name = 'pages/products.html'
    page_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(CategoriesListView, self).get_context_data(**kwargs)

        context['categories'] = ProductCategory.objects.filter(status=ProductPost.STATUS_IS_PUBLISHED)

        return context
