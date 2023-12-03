from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

from .models import Matiere, Note
from .models import Niveau
from .models import Eleve
from .forms import NoteForm
from django.contrib.auth import authenticate



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


            


def add_note(request, eleve_id, matiere_id):
    if request.user.is_authenticated:
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


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...