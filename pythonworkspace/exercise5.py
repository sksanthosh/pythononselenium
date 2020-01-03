#Script which takes month number from user and displays the no of days in it
month=int(input("Enter the month to check the no of days in it: "))
if month >= 1 and month < 13:
    if month == 1:
        m = 'JAN'
    elif month == 2:
        m = 'FEB'
    elif month == 3:
        m = 'MAR'
    elif month == 4:
        m = 'APR'
    elif month == 5:
        m = 'MAY'
    elif month == 6:
        m = 'JUN'
    elif month == 7:
        m = 'JUL'
    elif month == 8:
        m = 'AUG'
    elif month == 9:
        m = 'SEP'
    elif month == 10:
        m = 'OCT'
    elif month == 11:
        m = 'NOV'
    else:
        m = 'DEC' 
    if month==2:
        days=28
    elif month==1 or month==3 or month==5 or month==7 \
    or month==8 or month==10 or month==12:
        days=31
    else:
        days=30
    print("For",m,"it has",days,"days in it")
else:
    print("Enter the valid month to display the numbers in it")
