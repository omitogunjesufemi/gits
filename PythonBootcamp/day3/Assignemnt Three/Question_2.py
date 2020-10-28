# Finding future dates
today = int(input("Enter today's day: "))

if today in range(0,7):
    elapsed_days = int(input("Enter the number of days elapsed since today: "))
    future_days = (today + elapsed_days) % 7
else:
    print("Invalid Day")
    exit(0)

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(f"Today is {days_of_week[today]} and the future day is {days_of_week[future_days]}")