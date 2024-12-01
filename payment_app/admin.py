from django.contrib import admin
from .models import OtherData
from .models import Department, Fee

class FeeAdmin(admin.ModelAdmin):
  list_display = ['department', 'fee', 'amount']

class OtherDataAdmin(admin.ModelAdmin):
  list_display = ['level', 'semester']

admin.site.register(Department)
admin.site.register(Fee, FeeAdmin)
admin.site.register(OtherData, OtherDataAdmin)