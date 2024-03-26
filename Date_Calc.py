import datetime
 
now = datetime.datetime.today()

then = datetime.datetime(2010, 7, 18)

delta = now - then
print(delta.days)