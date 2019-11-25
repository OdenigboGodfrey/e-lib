from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(item)
admin.site.register(category)
admin.site.register(sub_category)
admin.site.register(item_type)
admin.site.register(borrowed)