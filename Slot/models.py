from django.db import models

# Create your models here.

from django.db import models

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10)
    status = models.CharField(
        max_length=10, 
        choices=(("available","Available"),("booked","Booked")), 
        default="available"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    slot_type = models.CharField(max_length=20, default="compact")

    def __str__(self):
        return self.slot_number

class Booking(models.Model):
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(
        max_length=10, 
        choices=(("confirmed","Confirmed"),("cancelled","Cancelled")), 
        default="confirmed"
    )

    def __str__(self):
        return f"{self.slot.slot_number} - {self.start_time}"
