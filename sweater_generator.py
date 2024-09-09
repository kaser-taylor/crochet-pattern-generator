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


def get_width_height(swatch_size):
    dimensions = swatch_size.split('x')
    width = dimensions[0]
    height = dimensions[1]
    return (width, height)

def calc_stitch_height(height, stitch_count):
    stich_height = height / stitch_count
    return stich_height

def calc_stitch_width(width, stitch_count):
    stitch_width = width / stitch_count
    return stitch_width

user_size = input('Please input your size: S M L XL XXL ').strip().lower()

user_measurements = get_measurements(user_size)

for key in user_measurements:
    print(key, user_measurements[key])

user_adjustments(user_measurements)

if user_adjustments == 'Invalid response':
    user_adjustments(user_measurements)

double_check_measurements = input('are these measurements correct? y or n ').strip().lower()

if double_check_measurements == 'n':
    user_adjustments(user_measurements)

swatch_size = input('input the size of your swatch in this format. The first number is width, the second is height. ex. 4x4 ')
vertical_stitches = int(input('input the number of rows in your swatch '))
horizontal_stitches = int(input('input how many stitches across your swatch is '))

swatch_height = int(get_width_height(swatch_size)[1])
swatch_width = int(get_width_height(swatch_size)[0])

stitch_height = calc_stitch_height(swatch_height, vertical_stitches)
stitch_width = calc_stitch_width(swatch_width, horizontal_stitches)

print(stitch_height)
print(stitch_width)