import math

# y = ax^2 + bx + c

def calculate_parabola_slope(x, c):
    y = 0
    x = x / 2
    c = c
    slope = round((y - c) / (x ** 2), 4)

    return slope

def find_x_vertical(a, c, y):
    x = round(math.sqrt((y - c) / a), 4)
    return x

def find_x_horizontal(rows, stitch_height):
    x = rows * stitch_height
    return x

def find_c_with_two_measurements(m1, m2):
    c = (m1 / 2) - (m2 / 2)

    return c

def find_y(a, x, c):
    y = ((a * (x ** 2)) + c)

    return y

def find_width_vertical(a, c, stitch_height, rows):
    row_widths = {}
    for i in range(rows):
        row_widths[f'row {i}'] = round(find_x_vertical(a, c, stitch_height * i), 4) * 2
    
    return row_widths

def find_width_horizontal(a, c, stitch_height, rows, m1, i_d):
    row_widths = {}
    if i_d == 'i':
        x = rows * stitch_height
        for i in range(rows):
            x -= stitch_height
            row_widths[f'row {i}'] = round(m1 - (find_y(a, x, c) * 2))
    else:
        x = 0
        for i in range(rows):
            x += stitch_height
            row_widths[f'row {i}'] = round(m1 - (find_y(a, x, c) * 2))

def calculate_stitches_per_row(row_widths, stitch_width):
    stitches_per_row = {}
    for row in row_widths:
        stitches_per_row[f'{row}'] = int(row_widths[row] / stitch_width)
        
    return stitches_per_row

def calculate_id_rows(stitches_per_row):
    id_between_rows = {}

    for i in range(len(stitches_per_row) - 1):
        id_between_rows[f'row {i} - {i+1}'] = stitches_per_row[f'row {i + 1}'] - stitches_per_row[f'row {i}']

    return id_between_rows

def put_it_all_together_vertical(upper_arm_circ, arm_hole_depth, stitch_height, rows, stitch_width):
    parabola_slope = calculate_parabola_slope(upper_arm_circ, arm_hole_depth)
    row_widths = find_width_vertical(parabola_slope, arm_hole_depth, stitch_height, rows)
    stitches_per_row = calculate_stitches_per_row(row_widths, stitch_width)
    decreases = calculate_id_rows(stitches_per_row)

    return decreases

def put_it_all_together_vertical(m1, m2, x):
    c = find_c_with_two_measurements(m1, m2)
    a = calculate_parabola_slope(x, c)
    row_widths = find_width_horizontal()