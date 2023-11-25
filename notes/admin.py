from django.contrib import admin

from notes.models import Eleve, Enseignant, Matiere, Niveau, Note

# Register your models here.
admin.site.register(Matiere)
admin.site.register(Eleve)
admin.site.register(Enseignant)
admin.site.register(Niveau)
admin.site.register(Note)