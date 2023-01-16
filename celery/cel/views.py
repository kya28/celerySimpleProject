from django.shortcuts import render
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact
from .service import send
from .tasks import send_spam_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'cel/contact.html'

    def form_valid(self, form):
        form.save()
        #send(form.instance.email)
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
