from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse

app_url = 'https://treso.fpma.re'
from_noreply = 'FPMA Réunion<fpmareunion@gmail.com>'
admin_mail = 'd.rajaonson@gmail.com'

def alerte_inscription(participant):
    params = {
        'obj': participant,
    }
    msg_plain = render_to_string('emails/alert_inscription.txt', params)
    
    email = EmailMessage(
        'FPMA Réunion - Inscription ' + str(participant.number) + ' pers - ' + participant.name,
        msg_plain,
        from_noreply,
        [participant.email],
        [admin_mail],
    )
    email.send()