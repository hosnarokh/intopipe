from django.contrib import admin

from .models import Customer, Material, Order


@admin.register(Material)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'created_time', 'updated_time']
    search_fields = ('title',)
    list_filter = ['active', ]
    readonly_fields = ['updated_time', 'created_time', ]
    fields = [
        'title',
        'active',
        'created_time',
        'updated_time',
        'description',
    ]


class OrderInline(admin.TabularInline):
    model = Order
    extra = 1
    readonly_fields = ['updated_time', 'created_time', ]
    fields = (
        'material',
        ('status', 'active'),
        'inner_diameter',
        'thickness',
        'length',
        'quantity',
        'created_time',
        'updated_time',
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status', 'active', 'created_time', 'updated_time']
    search_fields = ('name', 'email')
    list_filter = ['status', ]
    inlines = [OrderInline]
    readonly_fields = ['updated_time', 'created_time', ]
    fields = [
        ('name', 'email','phone'),
        ('status', 'active'),
        'website',
        'logo',
        'created_time',
        'updated_time',
        'description',
    ]
