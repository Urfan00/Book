from celery import shared_task
from Account.models import Account
from django.conf import settings
from .models import Subscriber
from Recipe.models import Recipes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    recipes = Recipes.objects.all()[:3]
    message =  render_to_string('email-subscribers.html', {
            "recipes" : recipes
        })
    subject = 'New Products From Our Website'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'html'
    mail.send()