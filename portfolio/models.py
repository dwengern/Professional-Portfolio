from django.db import models
from django.utils import timezone

class ValetCars(models.Model):
    ticketNum = models.IntegerField(primary_key=True)
    lastName = models.CharField(max_length=50)
    departureDate = models.DateTimeField()
    carMake = models.CharField(max_length=50)
    carModel = models.CharField(max_length=50)
    carColor = models.CharField(max_length=50)

    def __str__(self):
        return f"ValetCar Ticket number: {self.ticketNum}"

    
def get_model_by_name(model_name):
    model_mapping = {
        'valetcars': (ValetCars, ['ticketNum', 'lastName', 'departureDate', 'carMake', 'carModel', 'carColor']),
    }
    return model_mapping.get(model_name.lower())
