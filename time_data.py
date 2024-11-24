
from datetime import datetime, timezone, timedelta

# Get current UTC time
print('Israel', datetime.now())
print('UTC   ', datetime.now(timezone.utc))
print(datetime.now().strftime("%H:%M:%S.%f %d/%m/%Y"))
print(datetime.now().strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print( (datetime.now() + timedelta(days=1)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print( (datetime.now() + timedelta(days=30)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print( (datetime.now() + timedelta(hours=90)) .strftime("%H:%M:%S.%f %Y-%B-%d %A"))