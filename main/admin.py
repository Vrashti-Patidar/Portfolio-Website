from django.contrib import admin
from .models import Contact
# Register your models here.
# admin.site.register(Contact)  (for object)
@admin.register(Contact)
class UserModel(admin.ModelAdmin):
    list_display=['id','name','email','message']