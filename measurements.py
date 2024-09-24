s = {
    'bust': 35,
    'body length': 23,
    'sleeve length': 22,
    'shoulder width': 14.5,
    'arm hole depth': 7.5,
    'waist': 31,
    'hip': 35,
    'wrist': 6.25,
    'neck': 19,
    'upper arm circ': 11.5
}

m = {
    'bust': 39,
    'body length': 24,
    'sleeve length': 23,
    'shoulder width': 15.5,
    'arm hole depth': 8.5,
    'waist': 33,
    'hip': 39,
    'wrist': 6.65,
    'neck': 21,
    'upper arm circ': 13
}

l = {
    'bust': 43,
    'body length': 25,
    'sleeve length': 24,
    'shoulder width': 16.5,
    'arm hole depth': 9.5,
    'waist': 37,
    'hip': 43,
    'wrist': 7.25,
    'neck': 23,
    'upper arm circ': 14.5
}

xl = {
    'bust': 47,
    'body length': 26,
    'sleeve length': 25,
    'shoulder width': 17.5,
    'arm hole depth': 10.5,
    'waist': 41,
    'hip': 47,
    'wrist': 7.75,
    'neck': 25,
    'upper arm circ': 16
}

xxl = {
    'bust': 51,
    'body length': 27,
    'sleeve length': 26,
    'shoulder width': 18.5,
    'arm hole depth': 11.5,
    'waist': 45,
    'hip': 51,
    'wrist': 8.25,
    'neck': 27,
    'upper arm circ': 17.5
}

#gets the measurements of the project 
def get_size():
    user_size = input('Please input your size: S M L XL XXL ').strip().lower()

    return user_size

def get_measurements(size):
    if size == 's':
        return s
    elif size == 'm':
        return m
    elif size == 'l':
        return l
    elif size == 'xl':
        return xl
    elif size == 'xxl':
        return xxl
    else:
        return('Sizing option not available')

def user_adjustments(user_measurements):
    y_or_n = input('Would you like to make measurement adjustments? y or n ').strip().lower()
    if y_or_n == 'n':
        return('Okay!!')
    elif y_or_n == 'y':
        stop = False
        while stop != True: 
            measurement_to_adjust = input('Input value to adjust, s to exit ')
            if measurement_to_adjust == 's':
                stop = True
            else:
                measurement = int(input())
                user_measurements[measurement_to_adjust] = measurement
                print(user_measurements[measurement_to_adjust])
        else:
            for key in user_measurements:
                print(key, user_measurements[key])
            return(user_measurements)
    else:
        return('Invalid response')

user_measurements = get_measurements(get_size())