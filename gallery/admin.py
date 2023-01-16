from django.contrib import admin

from gallery.models import Photography

class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'legend')
    #list_display_links = '' clicable itens;
    search_fields = ('name',)

# Register your models here.
admin.site.register(Photography, PhotographyAdmin)