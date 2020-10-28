def main():
    calendar_width = 30
    read_year = int(input("Enter the year: "))
    read_start_day = int(input("Enter the day of January first (0: Sunday, 1: Monday,...,6: Saturday): "))
    days_of_week_line = "Sun Mon Tue Wed Thu Fri Sat ".ljust(calendar_width)
    day_cell_width = 4

    generate_month_body(month)


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def generate_month_body(month):
    get_number_of_days()
    for month in months_map:
        month_header = f"{month} {year}".center(calendar_width)
        month_body = f"{month_header}\n{days_of_week_line}\n"
    
    generate_days_of_month()


def read_start_day():
    start_day = read_start_day

def read_year():
    year = read_year

def get_number_of_days(month):
    months_map = {
        "January":31,
        "February": 29 if is_leap_year else 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }


def generate_days_of_month(month):
    get_number_of_days()
    for month in months_map:
        no_of_days = months_map[month]
        end_day = current_day + no_of_days
        start_day = current_day
        line = ""

        for day in range(0, end_day):
            if day < start_day:
                line += "".ljust(day_cell_width)
            else:
                line += str(day - start_day + 1).ljust(day_cell_width)
                current_day += 1
                current_day %= 7
                if current_day == 0 or day == end_day - 1:
                    month_body += line.ljust(calendar_width)
                    month_body += "\n"
                    line = ""