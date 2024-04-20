from django.contrib import admin

# Register your models here.

from .models import User, Poste, Recommandation, Transport, Logement, Stage
from .models import Reaction, Evenement, EvenClub

admin.site.register(User)
admin.site.register(Poste)
admin.site.register(Recommandation)
admin.site.register(Transport)
admin.site.register(Logement)
admin.site.register(Stage)
admin.site.register(Reaction)
admin.site.register(Evenement)
admin.site.register(EvenClub)

# Compare this snippet from studentHelp/models.py:


