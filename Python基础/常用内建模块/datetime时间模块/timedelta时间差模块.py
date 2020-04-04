from datetime import datetime,timedelta

Date=datetime.now().date()
Datetime=datetime.now()
print(Date)
print(Datetime)
print(Datetime+timedelta(weeks=1,days=1))
