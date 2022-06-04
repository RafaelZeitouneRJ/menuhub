from django.contrib import admin

# Register your models here.

from menus.models import Restaurant , MenuItem

# Esses modelos foram registrados para serem usados pela interface do Admins
admin.site.register(Restaurant)
admin.site.register(MenuItem)
