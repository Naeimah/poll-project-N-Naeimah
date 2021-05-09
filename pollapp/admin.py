from django.contrib import admin

# Register your models here.
from.models import poll 
from.models import option
from.models import response

class polladmin (admin.ModelAdmin):
  list_display = ("question", "active_until", "status",)
  list_filter = ("status",)
  search_fields = ("question",)

admin.site.register(poll)
admin.site.register(option)
admin.site.register(response)





