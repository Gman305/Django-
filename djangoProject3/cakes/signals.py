from random import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver
import random

from cakes.models import Cake, Baker


@receiver(pre_delete, sender=Baker)
def my_pre_delete(sender, instance, **kwargs):
    cakes=Cake.objects.filter(baker=instance).all()

    other_bakers=Baker.objects.exclude(id=instance.id).all()

    for cake in cakes:
        new_baker=random.choice(other_bakers)
        cake.baker=new_baker
        cake.save()