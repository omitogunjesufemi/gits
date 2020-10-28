import calendar

user_year, first_day = map(int, input("Enter the year and the first day: ").split(","))

output_calendar = calendar.calendar(user_year, 2, 1, 6)

print(output_calendar)