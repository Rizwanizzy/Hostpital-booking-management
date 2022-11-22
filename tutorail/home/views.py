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
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = request.POST['p_name']
            num = request.POST['p_phone']
            date = request.POST['booking_date']
            doc = request.POST['doc_name']
            Dr = doctors.objects.get(pk=doc)
            try:
                sid = 'AC2daf97d087da75d0d9677317d68d4ef1'
                # auth_token is temporary , it should be updated from twilio account when run this program
                auth_token = 'b2bcd513be49e4c122cfc9ecf29fc4fb'
                client = Client(sid, auth_token)
                # client.messages.create(body='CITY HOSPITAL:-Your booking is successful for Date:'+date+' with
                # Doctor: '+str(name) , from_='+14254751055', to='str(num)')
                client.messages.create(
                    body='CITY HOSPITAL:-Hi ' + name + 'Your booking is successful for Date:' + date + ' with Doctor: ' + str(
                        Dr) + 'Contact Number:' + str(num),
                    from_='+14254751055', to='+919037166884')

            except:
                messages.error(request, 'auth_token is temporary , it should be updated from twilio account when run '
                                        'this program')
                return redirect('booking')

            # print('phone number:', num, 'booked:', date, 'doctor name:', Dr)
            form.save()
            messages.success(request, f'Booking confirm successfully')
    form = BookingForm()

    dict_form = {
        'form': form,

    }
    return render(request, 'booking.html', dict_form)


def contact(request):
    return render(request, 'contact.html')


def doctor(request):
    dict_doc = {
        'doctors': doctors.objects.all()
    }
    return render(request, 'doctor.html', dict_doc)


def department(request):
    dict_dept = {
        'dept': departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)
