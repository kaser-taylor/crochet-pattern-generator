import measurements
import stitch_swatch_data
import print_increases
import math

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

def calc_row_gauge(height, vertical_stitch_count):
    stich_height = height / vertical_stitch_count
    return stich_height

def calc_stitch_width(width, stitch_count):
    stitch_width = width / stitch_count
    return stitch_width

def calc_stitch_gauge(width, height, vertical_stitches, horizontal_stitches):
    area = width * height
    total_stitches = vertical_stitches * horizontal_stitches
    stitches_per_inch = area // total_stitches
    return stitches_per_inch




# gets the size of the project
user_size = input('Please input your size: S M L XL XXL ').strip().lower()

#gets the measurements of the project 
user_measurements = get_measurements(user_size)

#prints measurements for user tso they can validate
for key in user_measurements:
    print(key, user_measurements[key])

#allows user to adjust measurements
user_adjustments(user_measurements)

#makes sure user input is valid and makes sure the measurements are correct
if user_adjustments == 'Invalid response':
    user_adjustments(user_measurements)

double_check_measurements = input('are these measurements correct? y or n ').strip().lower()

if double_check_measurements == 'n':
    user_adjustments(user_measurements)


#gets swatch data from user and defines proper variables
swatch_size = input('input the size of your swatch in this format. The first number is width, the second is height. ex. 4x4 ')
vertical_stitches = int(input('input the number of rows in your swatch '))
horizontal_stitches = int(input('input how many stitches across your swatch is '))
stitch_type = input('input the stitch used for swatch ')
swatch_height = int(get_width_height(swatch_size)[1])
swatch_width = int(get_width_height(swatch_size)[0])

#variables calculated from swatch data
row_gauge = calc_row_gauge(swatch_height, vertical_stitches)
stitch_width = calc_stitch_width(swatch_width, horizontal_stitches)
stitch_gauge = calc_stitch_gauge(swatch_width, swatch_height, vertical_stitches, horizontal_stitches)

#defines variable data for sleeves
sleeve_cap_rows = int(user_measurements['arm hole depth'] * row_gauge)
sleeve_rows = int((user_measurements['sleeve length'] * row_gauge) - sleeve_cap_rows)

sleeve_stitches_at_top = int((user_measurements['upper arm circ'] + 1) * stitch_gauge)
sleeve_cap_top_stitches = sleeve_stitches_at_top // 2

stitches_at_wrist = int((user_measurements['wrist'] + 1) * stitch_gauge)

sleeve_total_increase = sleeve_stitches_at_top - stitches_at_wrist
sleeve_rows_between_increase = sleeve_rows // sleeve_total_increase
sleeve_stitch_increase = 2

sleeve_cap_total_decrease = sleeve_stitches_at_top - sleeve_cap_top_stitches
sleeve_cap_rows_between_decrease = sleeve_cap_rows // sleeve_cap_total_decrease
sleeve_cap_stitch_decrease = 2


def generate_row_1(stitch_type, stitches_at_wrist):
    stitch = stitch_swatch_data.crochet_stitches[stitch_type]
    ch_increment = stitch_swatch_data.row_start_stitch_type_int[stitch]
    print(f'Row 1: Ch {stitches_at_wrist + ch_increment}; {stitch} in {ch_increment} from hook in each ch across ')

print_increases.print_rows(sleeve_rows, sleeve_rows_between_increase, stitch_type)
print(sleeve_rows)   
print(sleeve_rows_between_increase)
       
    

## remember to add 2 inches to bust wait & hips for ease
