from django.db import models

# Create your models here.
class Niveau(models.Model):
    nom = models.CharField(max_length=2,unique=True)

    def __str__(self) -> str:
        return self.nom

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(choices=(("M", "Masculin"), ("F","Feminin")),max_length=20)
    date_naissance = models.DateField()

    class Meta:
        abstract = True

   

class Enseignant(Personne):
    pass

    def __str__(self) -> str:
        return self.nom
    
    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

class Matiere(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    niveaus = models.ManyToManyField(Niveau)

    def __str__(self) -> str:
        return self.nom
    
    class Meta:
        verbose_name = "Matiere"
        verbose_name_plural = "Matieres"
        

class Eleve(Personne):
    id = models.BigIntegerField(primary_key=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
   # matieres = models.ManyToManyField(Matiere)

    def __str__(self) -> str:
        return self.nom + '\n'

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"
        
class Note(models.Model):
    valeur = models.FloatField(null=True)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.valeur)
    
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

