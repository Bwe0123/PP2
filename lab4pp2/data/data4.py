import datetime

today = datetime.datetime.now()
tomorrow=today + datetime.timedelta(days=1)
alpha=tomorrow - today
print(alpha.total_seconds(),"seconds")