from django.contrib import admin
from .models import CurrentOffer,Category,Product

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(CurrentOffer,AuthorAdmin)
admin.site.register(Category,AuthorAdmin)
admin.site.register(Product,AuthorAdmin)


admin.site.site_header = "সদাই অনলাইন দোকান"
admin.site.site_title = "গ্রামীণ খাদ্য সরবরাহকারী"
admin.site.index_title = "সূচী পৃষ্ঠা"
