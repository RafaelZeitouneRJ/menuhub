from django.contrib import admin

# Register your models here.

from menus.models import Restaurant , MenuItem

# Esses modelos foram registrados para serem usados pela interface do Admin
admin.site.register(Restaurant)
admin.site.register(MenuItem)
