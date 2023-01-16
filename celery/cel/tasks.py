import sys

from celery_main.celery import app
from django.core.mail import send_mail

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'You subscribed to the mailing list',
            'we will send spam every ten minutes',
            'albertto28@mail.ru',
            [contact.email],
            fail_silently=False,
        )


@app.task
def my_task(a, b):
    c = a + b
    return c


@app.task
def my_task_ass(d, e):
    c = d + e
    return c