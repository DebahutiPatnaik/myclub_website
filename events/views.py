from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    #return render(request,'home.html',{})
    name ="Debahuti"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number= int (month_number)
    cal = HTMLCalendar().formatmonth(year,month_number)
    now = datetime.now()
    time= now.strftime('%I:%M:%S %p')
    #time= now.time
    current_year= now.year
    return render (request,
                   'events/home.html',{
                       "name": name,
                       "year":year,
                       "month":month,
                       "month_number":month_number,
                       "cal":cal,
                       "current_year": current_year,
                       "time": time,
                    
                   })