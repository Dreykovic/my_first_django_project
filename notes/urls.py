from django.urls import path
from . import views
app_name ="notes"
urlpatterns = [
    path("", views.index, name="index"),
    path("eleves/", views.eleves, name="eleves"),
    path("eleve/<str:eleve_id>/", views.eleve, name="eleve"),
    path("matieres/", views.matieres, name="matieres"),
    path("matiere/<int:matiere_id>/", views.matiere, name="matiere"),
    path("niveau/<int:niveau_id>/", views.niveau, name="niveau"),
    path("add_note/<str:eleve_id>/<int:matiere_id>/", views.add_note, name="add-note"),
    path("eleves/pdf/", views.listeEleves, name="eleves-pdf"),
    path("elevesNiv/pdf/<int:niveau_id>", views.liste_niveauElv, name="eleves-niv-pdf"),
    path("notEleves/pdf/<int:matiere_id>", views.noteEleves, name="eleves-mat-pdf"),
    path("synthere/pdf/<str:eleve_id>", views.notesSynthese, name="synthese-pdf"),
    
    
    
]
