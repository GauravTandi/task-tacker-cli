import datetime 
print(datetime.__all__)
date = datetime.date.today()
now = datetime.datetime.now()
now = now.strftime("Date %d-%m-%y / %Hhr : %Mmin : %Ssec")
print(now)