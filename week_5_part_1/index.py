def next(date:str)->str:
    from datetime import datetime, timedelta
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(date, date_format)
    next_date_obj = date_obj + timedelta(days=1)
    return next_date_obj.strftime(date_format)

print(next("2023-03-14"))  # Output: "2023-03-15"