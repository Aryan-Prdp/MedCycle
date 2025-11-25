from celery import shared_task
from datetime import date, timedelta
from django.core.mail import send_mail
from .models import Medicine


# ------------------------------
# Check for Expiring Medicines (7 days)
# ------------------------------
@shared_task
def check_expiring_medicines():
    """
    Sends an email alert to users if any medicine
    is expiring within the next 7 days.
    """
    upcoming = date.today() + timedelta(days=7)

    expiring_meds = Medicine.objects.filter(
        expiry_date__lte=upcoming,
        donated=False
    )

    for medicine in expiring_meds:
        send_mail(
            subject="Medicine Expiry Alert",
            message=f"Your medicine '{medicine.name}' expires on {medicine.expiry_date}.",
            from_email="noreply@medcycle.com",
            recipient_list=[medicine.user.email],
            fail_silently=True,
        )

