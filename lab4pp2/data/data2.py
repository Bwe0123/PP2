import datetime

segodnya = datetime.date.today()
vchera=datetime.date.today()-datetime.timedelta(days=1)
tomorrow=segodnya+datetime.timedelta(days=1)

print(vchera) 
print(segodnya) 
print(tomorrow)