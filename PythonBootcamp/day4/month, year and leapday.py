month, year = eval(input("Enter the month number and year: "))

calendar_month1 = ("Months", "January", "February", "April", "May", "June", "July", "August", "September", "October", "November", "December")

pick_up = calendar_month1[month]

#january, march, may, july = 31
#august, october, december = 31
#february = 29 if isleap_year == True else 28
#april, june, september, november = 30

if (pick_up == "January") or (pick_up == "March") \
or (pick_up == "May") or (pick_up == "July") \
or (pick_up == "August") or (pick_up == "October") or (pick_up == "December"):
    print(f"{pick_up} {year} has 31 days")

elif (pick_up == "April") or (pick_up == "June") \
or (pick_up == "September") or (pick_up == "November"):
    print(f"{pick_up} {year} has 30 days")

elif pick_up == "February":
    if year % 4 == 0 and year % 100 != 0:
        print(f"{pick_up} {year} has 29 days")
    elif year % 400 == 0:
        print(f"{pick_up} {year} has 29 days")
    else:
        print(f"{pick_up} {year} has 28 days")


