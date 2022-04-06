from django.contrib import admin
from . models import Point
# Register your models here.
class PointAdmin(admin.ModelAdmin):
    list_display = ('address','humidity','Temperature','Location')
admin.site.register(Point,PointAdmin)