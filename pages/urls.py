from django.urls import re_path

from .views import ContactView, index, OurStoryView, SuccessView

app_name = 'pages'
urlpatterns = [
    re_path(r'^$', index, name='homepage'),
    re_path(r'^contact/$', ContactView.as_view(), name='contact'),
    re_path(r'^our-story/$', OurStoryView.as_view(), name='about'),
    re_path(r'^success/$', SuccessView.as_view(), name='success'),

]
