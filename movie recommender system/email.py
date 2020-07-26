from django.core.mail import send_mail
from django.conf import settings

from celergy_tasks.main import celergy_app

@celergy_app.task(name='send_verify_email')
def send_verify_email(to_email, verify_url):
	"""
    send the activation email
    : param to_email: receiver
    : param verify_url: activation url
    """
    
    subject = "Shopping mall verification"
    html_message = '<p> Dear Customer!</p>' \
                    '<p> Thanks for shopping on our website'\
                    '<p> Your activation email: %s. Please click here to activate it: </p>'\
                    '<p> <a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)
    
    send_mail(subject=subject,
            message='',
            from_email=settings.EMAIL_FROM,
            recipient_list=[to_mail],
            html_message=html_message)

