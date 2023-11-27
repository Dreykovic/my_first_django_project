from django import forms

from notes.models import Eleve, Note


class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ("valeur",)
        labels ={"valeur":"Note sur 20"}
        
class EleveForm(forms.ModelForm):
    
    class Meta:
        model = Eleve
        fields = "__all__"
        
