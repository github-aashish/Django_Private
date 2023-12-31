from django.contrib import admin
from .models import info_customer

# Register your models here.



class Info_Customer(admin.ModelAdmin):
    list_display = ["name","email","phone_no","message"]
admin.site.register(info_customer,Info_Customer)