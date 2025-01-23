print("Chapter#1, Exercise#3 : ")
from datetime import datetime
from datetime import date
today = date.today()
print("Today's date:", today)
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current time:",current_time)

