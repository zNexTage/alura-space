from django.contrib import admin

from gallery.models import Photography

class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('name', 'legend', 'is_published')
    #list_display_links = '' clicable itens;
    search_fields = ('name',)
    list_filter = ('category','user')
    list_per_page = 10 # ten itens per page
    list_editable = ('is_published',) # editable fields in table

# Register your models here.
admin.site.register(Photography, PhotographyAdmin)