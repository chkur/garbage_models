from django.contrib import admin

from main.models import Product, Selling


class SellingInline(admin.TabularInline):
    model = Selling
    readonly_fields = ["dt", "quantity", "order_data"]
    ordering = ["-dt"]
    extra = 0
    can_delete = False
    show_change_link = False

    def has_add_permission(self, request, obj):
        return False


@admin.register(Product)
class OrderRequestAdmin(admin.ModelAdmin):
    inlines = [
        SellingInline,
    ]
