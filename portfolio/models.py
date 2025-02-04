from django.db import models
from django.utils import timezone
import random

class ValetCars(models.Model):
    guestID = models.CharField(primary_key=True, max_length=5, unique=True)
    ticketNum = models.IntegerField()
    lastName = models.CharField(max_length=50)
    departureDate = models.DateTimeField()
    carMake = models.CharField(max_length=50)
    carModel = models.CharField(max_length=50)
    carColor = models.CharField(max_length=50)

    def __str__(self):
        return f"ValetCar Guest ID: {self.guestID}"
    
    def generate_guest_id(self):
        """Generates a random 5 digit guestID."""
        while True:
            guest_id = str(random.randint(10000, 99999))
            if not ValetCars.objects.filter(guestID=guest_id).exists():
                return guest_id
            
    def save(self, *args, **kwargs):
        if not self.guestID:
            self.guestID = self.generate_guest_id()
        super().save(*args, **kwargs)

    
def get_model_by_name(model_name):
    model_mapping = {
        'valetcars': (ValetCars, ['ticketNum', 'lastName', 'departureDate', 'carMake', 'carModel', 'carColor']),
    }
    return model_mapping.get(model_name.lower())
