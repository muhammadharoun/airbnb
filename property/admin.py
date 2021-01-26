from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Property , PropertyBook , Place , PropertyImages , PropertyReview , Category
# Register your models here
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Property , SomeModelAdmin)
admin.site.register(Place)
admin.site.register(PropertyBook)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
