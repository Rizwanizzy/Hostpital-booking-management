from django import forms
from .models import booking


# to display a date picker in BookingForm in booking.html as booking_date in widgets below
class DateInput(forms.DateInput):
    input_type = 'date'


# creating a form with booking table for users to input values
class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput()
        }
        # display the fields name of booking details in booking.html with our interest
        labels = {
            'p_name': 'Patient Name',
            'p_phone': 'Phone Number',
            'p_email': 'Patient Email',
            'doc_name': 'Doctor Name',
            'booking_date': 'Booking Date',
        }
