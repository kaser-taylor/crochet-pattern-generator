import math

# y = ax^2 + bx + c

def calculate_parabola_slope(upper_arm_circ, arm_hole_depth):
    y = 0
    x = upper_arm_circ / 2
    c = arm_hole_depth
    a = round((y - c) / (x ** 2), 4)

    return a

def find_x(a, arm_hole_depth, stitch_height):
    x = round(math.sqrt((stitch_height - arm_hole_depth) / a), 4)
    return x

def find_width(a, arm_hole_depth, stitch_height, rows):
    row_widths = {}
    for i in range(rows):
        row_widths[f'row {i}'] = round(find_x(a, arm_hole_depth, stitch_height * i), 4) * 2
    
    return row_widths

def calculate_stitches_per_row(row_widths, stitch_width):
    stitches_per_row = {}
    for row in row_widths:
        stitches_per_row[f'{row}'] = int(row_widths[row] / stitch_width)
        
    return stitches_per_row

def calculate_decrease(stitches_per_row):
    decrease_between_rows = {}

    for i in range(len(stitches_per_row) - 1):
        decrease_between_rows[f'row {i} - {i+1}'] = stitches_per_row[f'row {i + 1}'] - stitches_per_row[f'row {i}']

    return decrease_between_rows

def put_it_all_together(upper_arm_circ, arm_hole_depth, stitch_height, rows, stitch_width,):
    parabola_slope = calculate_parabola_slope(upper_arm_circ, arm_hole_depth)
    row_widths = find_width(parabola_slope, arm_hole_depth, stitch_height, rows)
    stitches_per_row = calculate_stitches_per_row(row_widths, stitch_width)
    decreases = calculate_decrease(stitches_per_row)

    return decreases

print(put_it_all_together(10, 10, 1, 10, .5))