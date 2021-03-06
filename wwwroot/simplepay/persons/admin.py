from django.contrib import admin
from .models import Tag, Person

class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tag Detail',          {'fields': ['name']}),
        ('Navigate Position',   {'fields': ('nav_display', 'home_display')}),
    ]
    list_display = ('name', 'nav_display', 'home_display')

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification',  {'fields':  ['name']}),
        ('Detail',          {'fields':  ('sex', 'age', 'active', 'tags')}),
    ]
    list_display = ('name', 'sex', 'age', 'active', 'pub_date', 'update_date')

admin.site.register(Tag, TagAdmin)
admin.site.register(Person, PersonAdmin)
