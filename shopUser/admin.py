from django.contrib import admin
from .models import CurrentOffer,Category

# Register your models here.
admin.site.register(CurrentOffer)
admin.site.register(Category)


admin.site.site_header = "সদাই অনলাইন দোকান"
admin.site.site_title = "গ্রামীণ খাদ্য সরবরাহকারী"
admin.site.index_title = "সূচী পৃষ্ঠা"
