import random

def get_numbers_ticket(min: int, max: int, quantity: int) ->list:
    my_range = range(min, max + 1)

    # Checking of valid input
    if not 1 <= min <= max <= 1000:
        print('Min should be less than max and max/min should be between 1 and 1000')
        return []
    # checking for valid quantity input
    elif len(my_range) < quantity:
        print('Quantity of numbers should be less than total quantity')
        return []
    # Using set for checking of uniqueness
    return (sorted(random.sample(my_range, quantity)))




if __name__ == '__main__':

    # exception handling
    try:
        input_str = list(map(int, input('Input your data for function  {min} {max} {quantity}:').split()))
        print(get_numbers_ticket(*input_str))
    except ValueError:
        print('Input data should be in this format: {min: int} {max: int} {quantity: int}')
