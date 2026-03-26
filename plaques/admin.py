# from django.contrib import admin
# from .models import Product, ProductCustomization, Category, Material, Fastening, Sticker, Order, Banner, Base, \
#     PlaqueShape, Feature, Dimension

# class ProductCustomizationInline(admin.TabularInline):
#     model = ProductCustomization
#     extra = 1

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'base_price', 'is_featured')
#     inlines = [ProductCustomizationInline]


# # plaques/admin.py

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     # REMOVE 'slug' from list_display
#     list_display = ('name', 'status')  # Change 'slug' to 'status' or just remove it

#     # REMOVE or comment out prepopulated_fields
#     # prepopulated_fields = {'slug': ('name',)}

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('order_number', 'full_name', 'status', 'created_at')
#     list_filter = ('status',)


# class DimensionAdmin(admin.ModelAdmin):
#     list_display = ('width', 'height', 'status')

# admin.site.register(Dimension, DimensionAdmin)


# # Register the rest of the models
# admin.site.register(Banner)
# admin.site.register(Material)
# admin.site.register(Fastening)
# admin.site.register(Sticker)
# admin.site.register(Base)
# admin.site.register(PlaqueShape)
# admin.site.register(Feature)
