from django.contrib import admin

from .models import User, Pet, Product, ProductImage, Chat, Message

# Register your models here.


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ]

    class Meta:
        model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Chat)
admin.site.register(Message)
