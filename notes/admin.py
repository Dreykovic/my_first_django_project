from django.contrib import admin
from notes.forms import EleveForm

from notes.models import  Eleve, Enseignant, Matiere, Niveau, Note


class EleveAdmin(admin.ModelAdmin):
    readonly_fields = ["sexe","nom","prenom"]
    form = EleveForm


# Register your models here.
admin.site.register(Matiere)
admin.site.register(Eleve,EleveAdmin)
admin.site.register(Enseignant)
admin.site.register(Niveau)
admin.site.register(Note)
