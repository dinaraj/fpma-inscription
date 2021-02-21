from django import forms
from .models import Participant


class InscriptionParticipant(forms.ModelForm):

    class Meta: 
        model = Participant
        fields = [
            'name', 
            'email', 
            'phone', 
            'number',
            'list_names',
        ]