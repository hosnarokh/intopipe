from django.contrib import admin

from .models import Contact, HomeFeature


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name',
                    'last_name',
                    'company',
                    'email',
                    'phone_number']
    search_fields = ['email']
    readonly_fields = ['first_name',
                       'last_name',
                       'company',
                       'email',
                       'phone_number',
                       'message', ]
    fields = ['first_name',
              'last_name',
              'company',
              'email',
              'phone_number',
              'message', ]


@admin.register(HomeFeature)
class HomeFeatureAdmin(admin.ModelAdmin):
    list_display = ['button_text', 'created_time', 'updated_time', 'active']
    fields = (
        'button_text',
        'active',
        'extra_file',
        'description'
    )
