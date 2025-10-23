from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import ParkingSlot, Booking
from django.contrib import messages

def view_slots(request):
    slots = ParkingSlot.objects.all()
    return render(request, "Slot/slots.html", {"slots": slots})

def book_slot(request, slot_id):
    slot = ParkingSlot.objects.get(id=slot_id)
    if request.method == "POST":
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        # Check for overlapping bookings
        conflict = Booking.objects.filter(
            slot=slot,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exists()

        if conflict:
            messages.error(request, "Slot already booked for this time!")
        else:
            Booking.objects.create(
                slot=slot,
                start_time=start_time,
                end_time=end_time,
                status="confirmed"
            )
            slot.status = "booked"
            slot.save()
            messages.success(request, "Booking successful!")
        return redirect("view_slots")

    return render(request, "Slot/book_slot.html", {"slot": slot})

def dashboard(request):
    bookings = Booking.objects.all().order_by('start_time')
    return render(request, "Slot/dashboard.html", {"bookings": bookings})

def cancel_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        booking.status = "cancelled"
        booking.slot.status = "available"
        booking.slot.save()
        booking.save()
        messages.success(request, "Booking cancelled successfully!")
    except Booking.DoesNotExist:
        messages.error(request, "Booking not found!")
    return redirect("dashboard")


def location_view(request):
    """
    Renders the live location tracking page.
    """
    return render(request, "Slot/location.html")