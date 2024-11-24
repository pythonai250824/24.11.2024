
from datetime import datetime, timezone, timedelta

# Get current UTC time
print('Israel', datetime.now())
print('UTC   ', datetime.now(timezone.utc))
print(datetime.now().strftime("%H:%M:%S.%f %d/%m/%Y"))
print(datetime.now().strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print( (datetime.now() + timedelta(days=1)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print( (datetime.now() + timedelta(days=30)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print( (datetime.now() + timedelta(hours=90)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))

# create a new list
# input names from the user until 'done'
# append each name to a list with a timestamp as tuple
# danny
#    0                        ,  1
# [ (datetime.now(), 'danny') , ( )]
# print all the time+name and index
# for key, value ...
#  0: danny 18:55  1: sharon 18:56