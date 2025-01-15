# need to change these to data classes for easier readability
s = {
    'bust': 35,
    'high chest': 31.5,
    'body length': 23,
    'sleeve length': 22,
    'shoulder width': 14.5,
    'arm hole depth': 7.5,
    'waist': 31,
    'hip': 35,
    'hip to waist': 8.5,
    'waist to bust': 8.75,
    'bust to neckline': 6.5,
    'wrist': 6.25,
    'neck': 19,
    'upper arm circ': 11.5
}

m = {
    'bust': 39,
    'high chest': 34.5,
    'body length': 24,
    'sleeve length': 23,
    'shoulder width': 15.5,
    'arm hole depth': 8.5,
    'waist': 33,
    'hip': 39,
    'hip to waist': 9,  
    'waist to bust': 9.25, 
    'bust to neckline': 7,
    'wrist': 6.65,
    'neck': 21,
    'upper arm circ': 13
}

l = {
    'bust': 43,
    'high chest': 37.5,
    'body length': 25,
    'sleeve length': 24,
    'shoulder width': 16.5,
    'arm hole depth': 9.5,
    'waist': 37,
    'hip': 43,
    'hip to waist': 9.5,
    'waist to bust': 9.75,
    'bust to neckline': 7.5,
    'wrist': 7.25,
    'neck': 23,
    'upper arm circ': 14.5
}

xl = {
    'bust': 47,
    'high chest': 44.6,
    'body length': 26,
    'sleeve length': 25,
    'shoulder width': 17.5,
    'arm hole depth': 10.5,
    'waist': 41,
    'hip': 47,
    'hip to waist': 10,
    'waist to bust': 10.25,
    'bust to neckline': 8,
    'wrist': 7.75,
    'neck': 25,
    'upper arm circ': 16
}

xxl = {
    'bust': 51,
    'high chest': 48.5,
    'body length': 27,
    'sleeve length': 26,
    'shoulder width': 18.5,
    'arm hole depth': 11.5,
    'waist': 45,
    'hip': 51,
    'hip to waist': 10.5,
    'waist to bust': 10.75,
    'bust to neckline': 8.5,
    'wrist': 8.25,
    'neck': 27,
    'upper arm circ': 17.5
}

baggy_factor = {
    'casual': 4,
    'oversized': 7,
    'tight': 2,
}

#gets the measurements of the project just used for user input. will be replaced with form arguments in the future 
def get_size():
    user_size = input('Please input your size: S M L XL XXL ').strip().lower()

    return user_size

# prints the preset measurements for the size the user inputs 
def get_measurements(size):
    if size == 's':
        print(s)
        return s
    elif size == 'm':
        print(m)
        return m
    elif size == 'l':
        print(l)
        return l
    elif size == 'xl':
        print(xl)
        return xl
    elif size == 'xxl':
        print(xxl)
        return xxl
    else:
        return('Sizing option not available')

#gathers user input on how baggy they want and sets the ease measurement to what the dictionary says. the dictionary later just adds that number to every measurement
def define_baggy_factor():
    user_input = input(f'What would you like the fit of your sweater to be? Casual, Oversized, Tight ').strip().lower()
    ease = baggy_factor[user_input]

    return ease

#gathers user input on if they want to keep their measurements, and what their swatch is like. This will be replaced by form input
def user_adjustments(user_measurements):
    final_measurements = user_measurements
    y_or_n = input('Would you like to make measurement adjustments? y or n ').strip().lower()
    if y_or_n == 'n':
        final_measurements = user_measurements
        return final_measurements
    elif y_or_n == 'y':
        stop = False
        while stop != True: 
            measurement_to_adjust = input('Input value to adjust, s to exit ').strip().lower()
            if measurement_to_adjust == 's':
                stop = True
            else:
                measurement = int(input())
                user_measurements[measurement_to_adjust] = measurement
                print(user_measurements[measurement_to_adjust])
        else:
            for key in user_measurements:
                print(key, user_measurements[key])
            final_measurements = user_measurements
            return final_measurements
    else:
        return('Invalid response')

# adds the ease to the final measurement. 
def processed_measurements(final_measurements, ease):
    for measurement in final_measurements:
        final_measurements[measurement] += ease
    return final_measurements
