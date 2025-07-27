import random

def get_numbers_ticket(min: int, max: int, quantity: int) ->set:
    my_range = range(min, max + 1)

    # Checking of valid input
    if min >= max:
        print('Min should be less than max')
        exit(1)
    elif min < 1 or min > 999 or max < 2 or max > 1000:
        print('Your max/min should be between 1 and 1000')
        exit(1)
    elif len(my_range) < quantity:
        print('Quantity of numbers should be less than total quantity')
        exit(1)
    # Using set for checking of uniqueness
    return set(random.sample(my_range, quantity))




if __name__ == '__main__':

    # exception handling
    try:
        input_str = list(map(int, input('Input your data for function  {min} {max} {quantity}:').split()))
        print(get_numbers_ticket(*input_str))
    except ValueError:
        print('Input data should be in this format: {min: int} {max: int} {quantity: int}')
        # the end)