from django.dispatch import Signal, receiver
from .models import Stuff

stuff_added_signal = Signal()

@receiver(stuff_added_signal)
def handle_stuff_added(sender, **kwargs):
    stuff = kwargs.get('stuff')
    print(f"A new item was added: {stuff.stuff_name}, Price: {stuff.price}")
