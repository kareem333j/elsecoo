from django.contrib import admin
from .models import Admin, PostsAdd,PostEdit,Product,Zapayn,ShopActivate,Offer
# Register your models here.

admin.site.register(Admin)
admin.site.register(PostsAdd)
admin.site.register(Product)
admin.site.register(PostEdit)
admin.site.register(Zapayn)
admin.site.register(ShopActivate)
admin.site.register(Offer)