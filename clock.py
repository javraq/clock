import datetime


class Time():

    def get_secs():

        x = datetime.datetime.now() 
        time = x.strftime("%X")
        # Provides hours mins 
        secs = time [6:9]
        return(secs)

    def get_mins():

        x = datetime.datetime.now() 
        time = x.strftime("%X")
        # Provides hours mins 
        mins = time[3:5]
        return(mins)

    def get_hours():
        x = datetime.datetime.now() 
        time = x.strftime("%X")
        # Provides hours mins 
        hours = time[0:2]
        return(hours)

clock =Time()
