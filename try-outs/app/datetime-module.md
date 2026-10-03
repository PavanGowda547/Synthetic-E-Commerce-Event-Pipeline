# datetime module

Python’s `datetime` module is a built-in module used to **work with dates and times** in a program. It allows us to get the current date and time, create and compare dates, add or subtract time, calculate durations, format dates, convert strings into dates, and handle different time zones. In data engineering, it is especially useful for tracking when data is created, received, processed, or loaded, managing incremental data pipelines, creating date-based partitions, detecting late or outdated data, calculating pipeline execution time, and handling time-based data accurately. In simple terms, **`datetime` helps a data pipeline understand and manage when things happen**.

List of operations we can perform on date and time :
- Getting the current date/time
- UTC timestamps
- Creating specific dates
- Extracting year, month, day, hour, etc.
- Date arithmetic with timedelta
- Incremental data loading
- Calculating date differences
- Formatting dates with strftime()
- Parsing strings into dates with strptime()
- Handling ISO 8601 timestamps
- Converting datetime to ISO format
- Time zones
- Converting between time zones
- Comparing dates
- Checking whether data is stale
- Creating rolling time windows
- Hourly processing windows
- Daily processing windows
- Generating date ranges
- Backfilling historical data
- Generating partition paths
- Generating partition keys
- Creating timestamped filenames
- Creating audit columns
- Tracking pipeline execution time
- Detecting late-arriving data
- Data freshness checks
- Expiration checks
- Data retention
- Finding weekdays/weekends
- Checking a specific day
- Month boundaries
- Start/end of a month
- Quarterly processing
- Financial/business dates
- Parsing database timestamps
- Handling Unix timestamps
- Converting datetime to Unix timestamp
- Validating incoming dates
- Detecting future timestamps
- Standardizing timestamps
- Handling timezone-aware vs naive datetime
- Building API extraction windows
