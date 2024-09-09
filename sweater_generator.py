import measurements

def get_measurements(size):
    if size == 's':
        return measurements.s
    elif size == 'm':
        return measurements.m
    elif size == 'l':
        return measurements.l
    elif size == 'xl':
        return measurements.xl
    elif size == 'xxl':
        return measurements.xxl
    else:
        return('Sizing option not available')

def user_adjustments(user_measurements):
    y_or_n = input('Would you like to make measurement adjustments? y or n').strip().lower()
    if y_or_n == 'n':
        return('Okay!!')
    elif y_or_n == 'y':
        stop = ''
        while stop != 's': 
            measurement_to_adjust = input('Input value to adjust, s to exit')
            measurement = int(input())
            user_measurements[measurement_to_adjust] = measurement
        else:
            return(user_measurements)
    else:
        return('Invalid response')

user_size = input('Please input your size: S M L XL XXL ').strip().lower()

user_measurements = get_measurements(user_size)

for key, value in user_measurements:
    print(key, value)

user_adjustments(user_measurements)

if user_adjustments == 'Invalid response':
    user_adjustments(user_measurements)

