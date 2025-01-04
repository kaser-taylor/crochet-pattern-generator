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
    c = abs((m1 / 2) - (m2 / 2))

    return c

def find_y(a, x, c):
    y = ((a * (x ** 2)) + c)

    return y

def find_width_vertical(a, c, stitch_height, rows):
    row_widths = {}
    for i in range(rows):
        row_widths[f'row {i}'] = round(find_x_vertical(a, c, stitch_height * i), 4) * 2
    
    return row_widths

def find_width_horizontal(a, c, stitch_height, rows, m1, x, i_d):
    row_widths = {}
    # i == true d == false
    if i_d == True:
        for i in range(rows):
            x -= stitch_height
            row_widths[f'row {i}'] = round(m1 - (find_y(a, x, c) * 2))
    else:
        for i in range(rows):
            x += stitch_height
            row_widths[f'row {i}'] = round(m1 - (find_y(a, x, c) * 2))

    return row_widths

def calculate_stitches_per_row(row_widths, stitch_width):
    stitches_per_row = {}
    for row in row_widths:
        stitches_per_row[f'{row}'] = int(row_widths[row] / stitch_width)
    print(stitches_per_row)    
    return stitches_per_row

def calculate_id_rows(stitches_per_row):
    id_between_rows = {}

    for i in range(len(stitches_per_row) - 1):
        id_between_rows[f'row {i} - {i+1}'] = stitches_per_row[f'row {i + 1}'] - stitches_per_row[f'row {i}']

    return id_between_rows

def put_it_all_together_vertical(x, y, stitch_height, rows, stitch_width):
    parabola_slope = calculate_parabola_slope(x, y)
    row_widths = find_width_vertical(parabola_slope, y, stitch_height, rows)
    stitches_per_row = calculate_stitches_per_row(row_widths, stitch_width)
    i_d = calculate_id_rows(stitches_per_row)

    return i_d

def put_it_all_together_horizontal(m1, m2, x, stitch_height, rows, stitch_width, i_d):
    c = find_c_with_two_measurements(m1, m2)
    a = calculate_parabola_slope(x, c)
    row_widths = find_width_horizontal(a, c, stitch_height, rows, m1, x, i_d)
    stitches_per_row = calculate_stitches_per_row(row_widths, stitch_width)

    return (stitches_per_row)