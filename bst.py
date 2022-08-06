# import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Create a timezone for Bangladesh Standard Time, UTC+6
bst = timezone(timedelta(hours=+6))

# August 6, 2022 at 12:23:34, UTC+6
dt = datetime(2022, 8, 6, 12, 23, 34, tzinfo=bst)

# Print Result
print(dt.isoformat())
