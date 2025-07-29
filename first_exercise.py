from datetime import datetime

"Main function which returns difference \
between some date and today"

def get_days_from_today(date: str):
    try:            # checking for mistakes
        date_struct = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return("Invalid format. Use format YYYY-MM-DD")
    today_date = datetime.today().date()
    days_difference = abs(today_date - date_struct).days
    return days_difference


"start my function"
if __name__ == '__main__':
    date_str = input("Enter a date(YYYY-MM-DD): ")
    print(get_days_from_today(date_str))
