from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    quantity    = models.PositiveIntegerField(default = 0)
    category    = models.ForeignKey(
                      Category,
                      on_delete=models.CASCADE,
                      related_name='products',
                      null=True, blank=True
                   )

    def __str__(self):
        return self.name
# Automatically check stock levels after saving a product
@receiver(post_save, sender=Product)
def notify_if_low_stock(sender, instance, **kwargs):
    try:
        # Forcefully convert to integer
        qty = int(instance.quantity) if instance.quantity is not None else 0
    except (TypeError, ValueError):
        return  # Skip if invalid

    # Compare after ensuring it's an integer
    if qty < 5:
        from .tasks import check_low_stock_and_notify
        check_low_stock_and_notify.delay()
