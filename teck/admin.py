from django.contrib import admin
from teck.models import Facilitators

# Register your models here.


class FacilitatorsAdmin(admin.ModelAdmin):
    list_display=('name','skill' , 'stack', 'organization', 'description')

admin.site.register(Facilitators, FacilitatorsAdmin)
