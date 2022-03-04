from django.urls import path, re_path

from .views import ProductsListView
from .views import MetalicPipeListView, MetalicPipeDetailView
from .views import PaperTubeListView, PaperTubeDetailView
from .views import PlasticPipeListView, PlasticPipeDetailView

app_name = 'products'
urlpatterns = [
    re_path(r'^$', ProductsListView.as_view(), name='products_list'),
    re_path(r'^paper-tube/$', PaperTubeListView.as_view(), name='paper-tube-list'),
    path('paper-tube/<slug:slug>/', PaperTubeDetailView.as_view(), name='paper-tube-detail'),
    re_path(r'^plastic-pipe/$', PlasticPipeListView.as_view(), name='plastic-pipe-list'),
    path('plastic-pipe/<slug:slug>/', PlasticPipeDetailView.as_view(), name='plastic-pipe-detail'),
    re_path(r'^metalic-pipe/$', MetalicPipeListView.as_view(), name='metalic-pipe-list'),
    path('metalic-pipe/<slug:slug>/', MetalicPipeDetailView.as_view(), name='metalic-pipe-detail'),

]
