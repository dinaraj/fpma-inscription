from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse

def alerte_inscription(participant, event):
    params = {
        'event': event,
        'obj': participant,
        'footer': event.email_footer,
    }
    msg_plain = render_to_string('emails/alert_inscription.txt', params)
    
    toBcc = []
    if event.email_alert: 
        toBcc = [event.email_alert]

    from_noreply = 'FPMA Réunion<fpmareunion@gmail.com>'
    if event.email_from: 
        from_noreply = event.email_from
    
    email = EmailMessage(
        event.paroisse + ' - Inscription ' + str(participant.number) + ' pers - ' + participant.name,
        msg_plain,
        from_noreply,
        [participant.email],
        toBcc,
    )
    email.send()