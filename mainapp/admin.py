from django.contrib import admin
from django.utils.html import mark_safe

from .models import Event, Participant
from import_export.admin import ImportExportMixin 

class ParticipantAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('__str__', 'accompagnants', 'created_at')

    def accompagnants(self, obj):
        return mark_safe(obj.list_names.replace("\n", "<br>"))

admin.site.register(Event)
admin.site.register(Participant, ParticipantAdmin) 