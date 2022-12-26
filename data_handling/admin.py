from django.contrib import admin

# Register your models here.
from .models import myrecord

admin.site.register(myrecord)


# for change django admin page header  

admin.site.site_header = "Nilanjan's data management Admin"
admin.site.index_title = "Welcome to Nilanjan's data management"
admin.site.site_title = "Data handling"