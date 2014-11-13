from celery.app import shared_task
from django.core.mail import send_mail

@shared_task
def send_email(topic, message, fr, to):
    send_mail(topic, message, fr, to)
