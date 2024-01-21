from django.contrib import admin
from .models import Author,Category,Journal,Image_Journal
# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Journal)
admin.site.register(Image_Journal)