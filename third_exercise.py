import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone_list(numbers: list) -> list:
    "******Main function which make our numbers clear****"
    clear_numbers = []
    for number in numbers:
        number = re.sub('[^0-9]', '', number) #remove all not number values
        if number.startswith('0') and len(number) ==  10: #here we add '+38' or '+'
            number = '+38' + number
        if number.startswith('38'):
            number = '+' + number
        clear_numbers.append(number)
    return clear_numbers # return list of numbers

"""
Print clear numbers
"""
print("Нормалізовані номери телефонів для SMS-розсилки:", *normalize_phone_list(raw_numbers), sep='\n')