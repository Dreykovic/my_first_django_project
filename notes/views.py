from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from Templating_ifnti.controlleur import generate_pdf

from .models import Matiere, Note
from .models import Niveau
from .models import Eleve
from .forms import NoteForm
from os.path import dirname, abspath

from django.contrib.auth.decorators import login_required, permission_required


def listeEleves(request):
    eleves = Eleve.objects.all()
    liste = {"eleves":eleves}
    print(liste)
    generate_pdf(liste)
    with open( dirname(dirname(abspath(__file__)))+ "/Templating_ifnti/out/liste_eleves.pdf", "rb") as my_file:
        return HttpResponse(my_file.read(), content_type = "application/pdf")

def liste_niveauElv(request, niveau_id):
    niveau = get_object_or_404(Niveau, pk= niveau_id)
    print(niveau)
    eleves = niveau.eleve_set.values()
    liste = {"eleves":list(eleves.values())}
    generate_pdf(liste)
    with open( dirname(dirname(abspath(__file__)))+ "/Templating_ifnti/out/liste_eleves.pdf", "rb") as my_file:
        return HttpResponse(my_file.read(), content_type = "application/pdf")
def index(request):
    return render(request, "notes/accueuil.html")


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


            


@login_required
@permission_required('notes.add_note', raise_exception=True)
def add_note(request, eleve_id, matiere_id):
    eleve = get_object_or_404(Eleve, pk=eleve_id)
    matiere = get_object_or_404(Matiere, pk=matiere_id)
    form = NoteForm()

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            valeur = form.cleaned_data.get("valeur")
            if matiere not in eleve.niveau.matiere_set.all():
                error_message = f"L'élève {eleve.nom} {eleve.prenom} ne suit pas le cours de matricule {matiere_id}"
                return HttpResponse(error_message)

            Note.objects.create(valeur=valeur, eleve=eleve, matiere=matiere)
            return render(request, "eleves/show.html", {"eleve": eleve})

    context = {"matiere": matiere, "eleve": eleve, "form": form}
    return render(request, "notes/add_note.html", context)

