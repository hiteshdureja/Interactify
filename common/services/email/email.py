from django.conf import settings
from django.core.mail import send_mail


class BaseEmailService:
    @staticmethod
    def trigger(to_email, subject, message):
        pass
        # send_mail(
        #     subject=subject,
        #     message=message,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[to_email],
        # )
