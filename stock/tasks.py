from celery import shared_task
from django.core.mail import mail_admins


@shared_task
def check_low_stock_and_notify():
    from .models import Product
    low = Product.objects.filter(quantity__lt=5)
    if low.exists():
        message = "\n".join(
          f"{p.name}: only {p.quantity} left" for p in low
        )
        mail_admins(
          subject="Low Stock Alert",
          message=message
        )
