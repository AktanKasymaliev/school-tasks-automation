from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from config.settings import EMAIL_HOST_USER, ALLOWED_HOSTS
from django.core.mail import send_mail

def send_email(student):
    current_site = ALLOWED_HOSTS[-1]
    context = {
        "small_text_detail": f"Hello, {student.full_name} you "
        "were added by teacher. "
        "Please read the mail "
        "we will let you know about new changes.",
        "email": student.email,
        "domain": current_site,
    }
    message = render_to_string('email/email.html', context)
    mail_subject = 'New School Generation greets you!'
    to_email = student.email
    send_mail(
        mail_subject,
        message,
        EMAIL_HOST_USER,
        [to_email, ],
        html_message=message,
    )