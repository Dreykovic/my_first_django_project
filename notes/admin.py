from django.contrib import admin
from notes.forms import EleveForm

from notes.models import  Eleve, Enseignant, Matiere, Niveau, Note
from import_export.admin import ImportExportModelAdmin
from import_export import resources #, fields
# from import_export.widgets import ForeignKeyWidget

#Eleve
class EleveAdmin(ImportExportModelAdmin):
    # readonly_fields = ["sexe","nom","prenom"]
    form = EleveForm
class EleveResource(resources.ModelResource):
    # niveau = fields.Field(
    #     column_name='niveau',
    #     attribute='niveau',
    #     widget=ForeignKeyWidget(Niveau, field='nom'))
    class Meta:
        model = Eleve
        resource_class = Eleve
        # fields = ("niveau",)
#Matiere        
class MatiereAdmin(ImportExportModelAdmin):
    pass
class MatiereResource(resources.ModelResource):
    class Meta:
        model = Matiere
        resource_class = Matiere
        
#Enseignant        
class EnseignantAdmin(ImportExportModelAdmin):
    pass
class EnseignantResource(resources.ModelResource):
    class Meta:
        model = Enseignant
        resource_class = Enseignant
        
#Note
class NoteAdmin(ImportExportModelAdmin):
    pass
class NoteResource(resources.ModelResource):
    class Meta:
        model = Note
        resource_class = Note
        
#Niveau
class NiveauAdmin(ImportExportModelAdmin):
    pass
class NiveauResource(resources.ModelResource):
    class Meta:
        model = Niveau
        resource_class = Niveau
    

# admin.site.register(Eleve, EleveAdmin)
# Register your models here.
admin.site.register(Matiere, MatiereAdmin)
admin.site.register(Eleve,EleveAdmin)
admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(Note, NoteAdmin)
