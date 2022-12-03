from django.contrib import messages
from django.shortcuts import render, redirect
from .models import departments, doctors
from .forms import BookingForm
from twilio.rest import Client


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    # when the button is clicked
    if request.method == 'POST':
        # retrieve the details given as input in form
        form = BookingForm(request.POST)
        # checking the details that are given is valid or not
        if form.is_valid():
            name = request.POST['p_name']
            num = request.POST['p_phone']
            date = request.POST['booking_date']
            doc = request.POST['doc_name']
            Dr = doctors.objects.get(pk=doc)
            try:
                # if the form is valid then send a sms to the user about the booking confirmation with the help of
                # twilio
                sid = 'AC2daf97d087da75d0d9677317d68d4ef1'
                # auth_token is temporary , it should be updated from twilio account when run this program
                auth_token = '5fa17xxxxxxxxxxxxxxxxxxxxxxbb9f5'
                client = Client(sid, auth_token)
                # client.messages.create(body='CITY HOSPITAL:-Your booking is successful for Date:'+date+' with
                # Doctor: '+str(name) , from_='+14254751055', to='str(num)')
                client.messages.create(
                    body='CITY HOSPITAL:-Hi ' + name + 'Your booking is successful for Date:' + date + ' with Doctor: ' + str(
                        Dr) + 'Contact Number:' + str(num),
                    from_='+14254751055', to='+919037166884')

            except:
                # when facing any issue with sending sms then display this error msg
                messages.error(request, 'auth_token is temporary , it should be updated from twilio account when run '
                                        'this program')
                return redirect('booking')

            # print('phone number:', num, 'booked:', date, 'doctor name:', Dr)
            # if the form is valid then save it
            form.save()
            messages.success(request, f'Booking confirm successfully')
    # render booking form fields that created in forms.py with table booking to booking.html
    form = BookingForm()
    dict_form = {
        'form': form,

    }
    return render(request, 'booking.html', dict_form)


def contact(request):
    return render(request, 'contact.html')


def doctor(request):
    # retrieving all data's from table doctors to a dictionary called dict_doc to display in doctor.html
    dict_doc = {
        'doctors': doctors.objects.all()
    }
    return render(request, 'doctor.html', dict_doc)


def department(request):
    # retrieving all data's from table departments to a dictionary called dict_dept to display in department.html
    dict_dept = {
        'dept': departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)
