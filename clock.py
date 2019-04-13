import datetime


class Time():
   """A class to import time and get hours, minutes and seconds"""    
    
    def get_secs():
        x = datetime.datetime.now() 
        time = x.strftime("%X")
        # Slices to seconds
        secs = time [6:9]
        return(secs)

    def get_mins():
        x = datetime.datetime.now() 
        time = x.strftime("%X")
        # Slices to minutes
        mins = time[3:5]
        return(mins)

    def get_hours():
        x = datetime.datetime.now() 
        time = x.strftime("%X")
        # Slices to hours 
        hours = time[0:2]
        return(hours)
