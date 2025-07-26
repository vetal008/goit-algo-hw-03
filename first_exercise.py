from datetime import datetime

"Main function which returns difference \
between some date and today"
def get_days_from_today(date: str) -> int:
    try:
        date_struct = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid format. Use format YYYY-MM-DD")
        exit(1)
    today_date = datetime.today()
    days_difference = abs(today_date - date_struct).days
    return days_difference


"start my function"
if __name__ == '__main__':
    date_str = input("Enter a date(YYYY-MM-DD): ")
    print(get_days_from_today(date_str))