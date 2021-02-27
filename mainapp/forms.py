from django import forms
from .models import Participant


class InscriptionParticipant(forms.ModelForm):

    number = forms.ChoiceField(label='Nombre de personnes au total', choices=[(x, str(x) + ' personne' + ('s' if x>1 else '')) for x in range(1,8)], required=True)

    class Meta: 
        model = Participant
        fields = [
            'name', 
            'email', 
            'phone', 
            'number', 
        ]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in range(1, 7):
            field_name = 'name_%s' % (i,)
            label = ""
            if i == 1:
                label = "Prénom des accompagnants (adulte ou enfant)"
            widget = forms.TextInput(attrs={
                'data-i': i, 
                'class': 'prenom_accomp', 
                'required': 'required', 
                'placeholder': 'Accompagnant #' + str(i)})
            self.fields[field_name] = forms.CharField(label=label, required=False,
                widget=widget)
    