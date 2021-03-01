from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

class Event(models.Model):
    name = models.CharField(_("Intitulé"), max_length=250)
    date = models.DateField(_("Date"))
    number_max = models.IntegerField(_("Capacité maximum"))
    active = models.BooleanField(_("Actif"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

class Participant(models.Model):
    event = models.ForeignKey(Event, verbose_name=_("Evénement"), on_delete=models.PROTECT, related_name='participants')
    name = models.CharField(_("Nom et prénom"), max_length=50)
    email = models.EmailField(_("Adresse mail"), max_length=250)
    phone = models.CharField(_("Numéro de téléphone"), max_length=15)
    number = models.IntegerField(_("Nombre de personnes"), validators=[MinValueValidator(1), MaxValueValidator(8)])
    list_names = models.TextField(_("Prénom des personnes"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name + ' (' + str(self.number) + ' pers.)'

    def __str__(self):
        return self.name + ' (' + str(self.number) + ' pers.)'
            