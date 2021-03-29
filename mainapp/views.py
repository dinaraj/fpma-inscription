from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime

from .forms import InscriptionParticipant
from .models import Participant, Event
from .mailer import alerte_inscription

def inscription(request, template='mainapp/inscription.html'):
    event = Event.objects.filter(active=True).latest('id')

    nbPlacesDispo = event.number_max
    nbPlacesReservees = event.participants.aggregate(Sum('number'))['number__sum'] or 0
    nbPlacesRestantes = nbPlacesDispo - nbPlacesReservees

    datestart = datetime.strptime('2021-03-29 22:05:00', '%Y-%m-%d %H:%M:%S')
    now = datetime.now()
    
    print(datestart)
    print(now)
    if datetime.now() <= datestart:
        return render(request, 'mainapp/inscription_too_early.html', {now: now})
    
    if nbPlacesRestantes <= 0:
        return render(request, 'mainapp/inscription_cloture.html')
    
    if request.method == 'POST':
        form = InscriptionParticipant(request.POST)
        if form.is_valid():
            cleaned_data = (form.cleaned_data)

            # Check places restantes
            if nbPlacesRestantes < int(cleaned_data['number']):
                messages.error(request, "Désolé, il ne reste plus que " + str(nbPlacesRestantes) + " places disponibles")
                return redirect("inscription")

            names = []
            for i in range(1,7):
                key = 'name_'+str(i)
                if key in cleaned_data and cleaned_data[key]:
                    names.append(cleaned_data[key])
            names_str = "\n".join(names)
            participant = form.save(commit=False)
            participant.event = event
            participant.list_names = names_str
            participant.save()

            # send mail admin + user
            alerte_inscription(participant, event)

            messages.success(request, "Votre inscription pour " + str(participant.number) + " personne(s) a bien été enregistrée")
            return redirect("inscription")
    else: 
        form = InscriptionParticipant()

    context = {
        'event': event,
        'form': form,
        'places_restantes': nbPlacesRestantes,
    }
    return render(request, template, context)

