def next(date:str)-> str:
    """Calculate the next date .
    >>> next('22/10/2008')
    '23/10/2008'
    """
    # Step 1: Extract the day, month and year 
    date = date.split('/')
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    

