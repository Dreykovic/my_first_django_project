import datetime
from enum import unique
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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
    id = models.CharField(primary_key=True, max_length=55)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
   # matieres = models.ManyToManyField(Matiere)

    def __str__(self) -> str:
        return self.nom + '\n'
    
    def clean(self) -> None:
        nom_contient_entier = any(caractere.isdigit() for caractere in self.nom)
        prenom_contient_entier = any(caractere.isdigit() for caractere in self.prenom)
        if(nom_contient_entier or prenom_contient_entier):
            raise ValidationError("Le nom et le prénom contiennt ne doivent contenir que des caractère alphabétiques")
    def save(self, *args, **kwargs):
        self.id = self.nom[slice(3)]
        self.id += str(datetime.datetime.now())
        self.id = self.id.replace(" ","")
        self.id = self.id.replace("-","")
        self.id = self.id.replace(":","")
        self.id = self.id.replace(".","")
    
        # Appelle la méthode save() du modèle parent pour effectuer la sauvegarde réelle
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"
        
class Note(models.Model):
    valeur = models.FloatField(null=True, validators=[MinValueValidator(0),MaxValueValidator(20)])
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.valeur)
  
    
    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

