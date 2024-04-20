from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telnumber = models.IntegerField(blank=True)   
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50 ,default='user')

    
#Poste Models 
class Poste(models.Model):
    image =models.ImageField(blank=True)
    POST_TYPE_CHOICES = (
        (0, "Offre"),  
        (1, "Demande"),
    )
    poste_type = models.IntegerField(choices=POST_TYPE_CHOICES)
    date_upload = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)





class Recommandation(Poste):
    texte = models.CharField(max_length=255)

class Transport(Poste):

    depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    heure_dep = models.TimeField()
    nbre_sieges = models.IntegerField()
    contact_Trans = models.CharField(max_length=255)

class Logement(Poste):

    localisation = models.CharField(max_length=255)
    description = models.TextField()
    logment_contact = models.CharField(max_length=255)

class Stage(Poste):
    typeStg = models.IntegerField(choices=[
        (1, 'Ouvrier'),
        (2, 'Technicien'),
        (3, 'PFE'),
    ])    
    societe = models.CharField(max_length=255)
    duree = models.IntegerField()
    sujet = models.CharField(max_length=255)
    contact_Stage = models.CharField(max_length=255)
    specialite = models.CharField(max_length=5, choices=[
        ('IT', 'IT - Technologie informatique'),
        ('SEG', 'SEG - Sc Eco et Gestion'),
        ('GC', 'GC - Génie Civil'),
        ('GP', 'GP - Génie des Procédés'),
        ('GM', 'GM - Génie Mécanique'),
    ])



class Reaction(models.Model):

    comment = models.TextField(max_length=999)
    like = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE)


# Evenement classes :  
class Evenement(Poste):
    intitule = models.CharField(max_length=255)
    description = models.TextField()
    lieu = models.CharField(max_length=255)
    contact_Event = models.CharField(max_length=255)

class EvenClub(Evenement):
    club = models.CharField(max_length=255)

class EvenSocial(Evenement):
    prix = models.FloatField()