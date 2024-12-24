from django.contrib import admin
from .models import YourModelName  # Replace with your actual model names

class YourModelNameAdmin(admin.ModelAdmin):  # Replace with your actual model admin class
    list_display = ('field1', 'field2')  # Replace with your actual fields
    search_fields = ('field1',)

admin.site.register(YourModelName, YourModelNameAdmin)  # Register your model admin class here