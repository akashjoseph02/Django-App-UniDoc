from django.shortcuts import render, redirect

# from .models import DocListItem

from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def appview(request):
    user_email = request.user.email
    all_items = Appointment.objects.filter(user = user_email)
    return render(request, 'dashboard.html', {'all_items' : all_items})

    

# @login_required(login_url='/login')
# def additem(request):
#     user_email = request.user.email
#     new_item = Appointment()
#     new_item.user = user_email
#     new_item.content = request.POST.get('content')
#     new_item.save()
#     return HttpResponseRedirect('/dashboard/')

@login_required(login_url='/login')
def validWeekday(days):
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, int(days)):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays



@login_required(login_url='/login')
def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y



@login_required(login_url='/login')
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays



@login_required(login_url='/login')
def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x



@login_required(login_url='/login')
def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x



@login_required(login_url='/login')
def booking(request):
    #Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    # weekdays = validWeekday(22)

    #Only show the days that are not full:
    # validateWeekdays = isWeekdayValid(weekdays) 
    validateWeekdays =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM", "6:30 PM", "7 PM", "7:30 PM"
    ]

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        time = request.POST.get('times')
        if service == None:
            messages.success(request, "Please Select A Service!")
            return redirect('booking')

        model = Appointment.objects.create(user=request.user.id,service=service,day=day,time=time)
        model.save()

        #Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service
        request.session['time'] = time

        return redirect('miniapp:dashboard')


    return render(request, 'booking.html', {'validateWeekdays': validateWeekdays, 'times':times})

@login_required(login_url='/login')
def userPanel(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('day', 'time')
    return render(request, 'userPanel.html', {
        'user':user,
        'appointments':appointments,
    }) 

@login_required(login_url='/login')
def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day', 'times')

    return render(request, 'staffPanel.html', {
        'items':items,
    })





# @login_required(login_url='/login')
# def bookingSubmit(request):
#     user = request.user
#     times = [
#         "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM", "6:30 PM", "7 PM", "7:30 PM"
#     ]
#     today = datetime.now()
#     minDate = today.strftime('%Y-%m-%d')
#     deltatime = today + timedelta(days=21)
#     strdeltatime = deltatime.strftime('%Y-%m-%d')
#     maxDate = strdeltatime

#     #Get stored data from django session:
#     day = request.session.get('day')
#     service = request.session.get('service')
    
#     #Only show the time of the day that has not been selected before:
#     hour = checkTime(times, day)
#     if request.method == 'POST':
#         time = request.POST.get("time")
#         date = dayToWeekday(day)

#         if service != None:
#             if day <= maxDate and day >= minDate:
#                 if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
#                     if Appointment.objects.filter(day=day).count() < 11:
#                         if Appointment.objects.filter(day=day, time=time).count() < 1:
#                             AppointmentForm = Appointment.objects.get_or_create(
#                                 user = user,
#                                 service = service,
#                                 day = day,
#                                 time = time,
#                             )
#                             messages.success(request, "Appointment Saved!")
#                             return redirect('index')
#                         else:
#                             messages.success(request, "The Selected Time Has Been Reserved Before!")
#                     else:
#                         messages.success(request, "The Selected Day Is Full!")
#                 else:
#                     messages.success(request, "The Selected Date Is Incorrect")
#             else:
#                     messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
#         else:
#             messages.success(request, "Please Select A Service!")


#     return render(request, 'bookingSubmit.html', {
#         'times':hour,
#     })


