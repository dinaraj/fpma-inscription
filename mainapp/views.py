from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import InscriptionParticipant
from .models import Participant, Event

def inscription(request, template='mainapp/inscription.html'):
    event = Event.objects.filter(active=True).latest('id')
    if request.method == 'POST':
        form = InscriptionParticipant(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = event
            participant.save()
            # TODO send mail admin + user
            messages.success(request, "Votre inscription pour " + str(participant.number) + " personne(s) a bien été enregistrée")
            return redirect("inscription")
    
    else: 
        form = InscriptionParticipant()

    context = {
        'event': event,
        'form': form,
    }
    return render(request, template, context)

