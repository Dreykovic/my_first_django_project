import locale
from urllib import response
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from .models import Matiere, Note
from .models import Niveau
from .models import Eleve


def index(request):
    return render(request, "notes/index.html")


def eleves(request):
    eleves = Eleve.objects.all()

    return render(request, "eleves/index.html", {"eleves": eleves})


def matieres(request):
    matieres = Matiere.objects.all()

    return render(request, "matieres/index.html", {"matieres": matieres})


def eleve(request, eleve_id):
    eleve = get_object_or_404(Eleve, pk=eleve_id)

    print(matieres)
    return render(request, "eleves/show.html", locals())


def matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, pk=matiere_id)
    return render(request, "matieres/show.html", locals())


def niveau(request, niveau_id):
    niveau = get_object_or_404(Niveau, pk=niveau_id)
    return render(request, "niveaus/show.html", locals())


            
def add_note(request, eleve_id, matiere_id):
    try:
        eleve = Eleve.objects.get( pk=eleve_id)
        matiere = Matiere.objects.get( pk=matiere_id)
    except ( Matiere.DoesNotExist) as e1:
        error_message = "Une erreur est survenue: La matière spécifiée n'existe pas."
        return HttpResponse(error_message)
    except (Eleve.DoesNotExist) as e2:
        error_message = "Une erreur est survenue: L'élève spécifié n'existe pas."
        return HttpResponse(error_message)

    if request.method == "POST":
        valeur = request.POST.get("valeur")
        Note.objects.create(valeur=valeur, eleve=eleve, matiere=matiere)
        return render(request, "eleves/show.html", {"eleve": eleve})

    if matiere not in eleve.niveau.matiere_set.all():
        error_message = f"Une erreur est survenue: L'élève {eleve.nom} {eleve.prenom} ne suit pas le cours de matricule {matiere_id}"
        return HttpResponse(error_message)

    return render(request, "notes/add_note.html", {"matiere": matiere, "eleve": eleve})
