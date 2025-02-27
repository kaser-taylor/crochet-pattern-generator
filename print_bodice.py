import math

def body_piece_length(body_length):
    bpl = body_length - 2
    
    return bpl

def bodice_rows(body_piece_length, stitch_height):
    rows = body_piece_length // stitch_height

    return rows

def find_widest(length_dict):
    widest = 0
    for value in length_dict.values():
        if int(value) > widest:
            widest = int(value)
    return widest

def stitches_per_row(widest_measure, stitch_width):
    spr = widest_measure // stitch_width

    return spr

def print_body_piece(rows, stitches_per_row, stitch):
    print(f'For {rows} rows, {stitch} {stitches_per_row}')
    print(f'Slip stitch and tie off row')

def print_neckline_statement():
    print(f'After finishing the body piece start on one end of the sweater for the neckline')

def neckline_rows(stitch_height):
    rows = int(2 / stitch_height)

    return rows

def find_x(stitch_height, rows):
    x_values = []
    for i in range(rows):
        x = math.sqrt(((i + 1) * stitch_height) / .1)
        x_values.append(x)
    return x_values

def find_widths(x_values, base_width):
    widths = []
    curr_width = base_width
    for x in x_values:
        curr_width = curr_width - 2 * x
        widths.append(curr_width)
    return widths

def find_stitches_per_row_neckline(widths, stitch_width):
    spr = []
    for width in widths:
        spr.append(width // stitch_width)
    return spr

def calculate_dec_neckline(spr, base_stitches):
    dec = []
    curr_stitch = base_stitches
    decrease = 0
    for row in spr:
        decrease = (curr_stitch - row)
        dec.append(decrease)
        curr_stitch -= decrease
    return dec
    

def print_neckline(decreases, base_stitches, stitch_type):
    stitch_count = base_stitches
    f_b = True
    for dec in decreases:
        if f_b == True:
            print(f'{stitch_type} {stitch_count - (2 * dec)} dec {dec}')
            stitch_count -= dec
            f_b = False
        else:
            print(f'dec{dec} {stitch_type} in the next {stitch_count - (2 * dec)}')
            stitch_count -= dec
            f_b = True
        print(stitch_count)
def print_body(body_length, stitch_height, body_widths, stitch_width, stitch):
    length_body_piece = body_piece_length(body_length)
    rows_body_piece = bodice_rows(length_body_piece, stitch_height)
    widest_point = find_widest(body_widths)

    spr = stitches_per_row(widest_point, stitch_width)
    body_print = print_body_piece(rows_body_piece, spr, stitch)    
    print_neckline_statement()
    neck_rows = neckline_rows(stitch_height)
    x_values = find_x(stitch_height, neck_rows)
    widths = find_widths(x_values, widest_point)
    print(widths)
    spr_neck = find_stitches_per_row_neckline(widths, stitch_width)
    print(spr_neck)
    decrease_neck = calculate_dec_neckline(spr_neck, spr)
    print(decrease_neck)
    neck_print = print_neckline(decrease_neck, spr, stitch)

