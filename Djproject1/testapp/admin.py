from django.contrib import admin
from testapp.models import hydjobs,punejobs,chennaijobs,blorejobs


class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility', 'address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class blorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
# Register your models here.

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
admin.site.register(blorejobs,blorejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
