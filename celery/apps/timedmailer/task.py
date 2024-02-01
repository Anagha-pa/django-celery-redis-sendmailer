from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

def send_ad_mails(self, target_mail, message):
    recipient_list = [target_mail]
    mail_subject = "You are on your luck day!"
    send_mail(
        subject = mail_subject,
        message = message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = recipient_list,
        fail_silently = False
    )
    return "Done" 