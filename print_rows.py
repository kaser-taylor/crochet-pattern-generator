import math
import quadratics
def print_regular_repeat(row_counter, rows_between, stitch):
    print(f'Row {row_counter} - {row_counter + rows_between} {stitch}')

def print_increase(row_counter, stitch):
    print(f'Row {row_counter} 2{stitch} in first st 2{stitch} in last')

def print_decrease(row_counter, stitch_count, stitch):
    print(f'Row {row_counter} {stitch}2tog, {stitch} in the next {stitch_count - 4}, {stitch}2tog')


# this pulls apart original print_rows function
def print_rows (tracked_data, rows_between, stitch, i_d):
    if tracked_data['increase'] == False:
            print_regular_repeat(tracked_data['row_counter'], rows_between, stitch)
            tracked_data['row_counter'] += (rows_between)
            tracked_data['increase'] = True
    else:
        if i_d == 'i':
            tracked_data['row_counter'] += 1
            print_increase(tracked_data['row_counter'], stitch)
            tracked_data['row_counter'] += 1
            tracked_data['increase_counter'] += 1
            tracked_data['increase'] = False
        else:
            tracked_data['row_counter'] += 1
            print_decrease(tracked_data['row_counter'], tracked_data['stitch_count'], stitch)
            tracked_data['row_counter'] += 1
            tracked_data['increase_counter'] += 1
            tracked_data['increase'] = False
            tracked_data['stitch_count'] -= 2

# This handles the while loop for printing the right amount of rows 
def row_tracker(rows, num_increases, rows_between, stitch, i_d='i', stitch_count=0, row_counter=2):
    tracking_data = {
        'row_counter': row_counter,
        'increase': False,
        'increase_counter': 0,
        'stitch_count': stitch_count
    }

    while tracking_data['row_counter'] < rows:
        if (tracking_data['row_counter'] + rows_between) >= rows:
            final_rows_between = int((rows - tracking_data['row_counter']) / (num_increases - tracking_data['increase_counter']))
            print_rows(tracking_data, final_rows_between, stitch, i_d)
            break
        else:
            print_rows(tracking_data, rows_between, stitch, i_d)
    
    while num_increases != tracking_data['increase_counter']:
        final_rows_between = int((rows - tracking_data['row_counter']) / (num_increases - tracking_data['increase_counter']))
        print_rows(tracking_data, rows_between, stitch, i_d)
    
    return tracking_data


def print_sleeve_cap(tracking_data, decrease_data, stitch, stitch_count):
    cap_tracker = tracking_data
    # {
    #     'row_counter'
    #     'increase'
    #     'increase_counter'
    #     'stitch_count'
    # }

    for row, value in decrease_data.items():
        f_b = calculate_f_and_b_dec(value)
        cap_tracker['row_counter'] += 1
        if stitch_count <= 0:
            break
        elif f_b['front_decrease'] == 0:
            stitch_count -= f_b['back_decrease'] * 2
            print(f"Row {cap_tracker['row_counter']} {stitch} in the next {stitch_count} dec{f_b['back_decrease']}")
            stitch_count += 1
            # stitch_count -= f_b['back_decrease']
        else:
            stitch_count -= f_b['front_decrease'] * 2
            stitch_count -= f_b['back_decrease'] * 2
            print(f"Row {cap_tracker['row_counter']} dec {f_b['front_decrease']} {stitch} in the next {stitch_count} dec{f_b['back_decrease']}")
            stitch_count += 2
            # stitch_count -= f_b['back_decrease']


        
    

def calculate_f_and_b_dec(decrease):
    decrease_data = {
        'front_decrease': 0,
        'back_decrease': 0
    }

    total_stitches = decrease

    while total_stitches < 0:
        if total_stitches % 2 == 0:
            decrease_data['front_decrease'] += 1
            
        else:
            decrease_data['back_decrease'] += 1
        
        total_stitches += 1
    
    return decrease_data
        
def compile_bodice_section_data(measurements):
  bodice_data = {
      'section_heights': [measurements['hip to waist'], measurements['waist to bust'], measurements['bust to neckline']],
      'bodice_widths': [measurements['hip'], measurements['waist'], measurements['bust'], measurements['high chest']]
  }
  return bodice_data
def print_section(stitches_per_row, stitch, row_count):
    for i in range(len(stitches_per_row) - 1):
        i_d = stitches_per_row[f'row {i + 1}'] - stitches_per_row[f'row {i}']
        if i_d == 0:
            print(f'Row {row_count[0] + 1} {stitch} in the next {stitches_per_row[f"row {i}"]}')
        elif i_d == -1:
            print(f'Row {row_count[0] + 1} dec 1 {stitch} in the next {stitches_per_row - 1}')
        elif i_d == 1:
            print(f'Row {row_count[0] + 1} inc 1 {stitch} in the next {stitches_per_row - 1}')
        elif i_d > 1:
            print(f'Row {row_count[0] + 1} inc {math.floor(i_d / 2)} {stitch} in the next {stitches_per_row[f"row {i}"] - math.floor(i_d / 2)} inc {math.ceil(i_d / 2)}')
        else:
            print(f'Row {row_count[0] + 1} dec {math.floor(abs(i_d / 2))} in the next {stitches_per_row[f"row {i}"] - math.floor(abs(i_d / 2))} dec {abs(math.ceil(i_d / 2))}')
        row_count[0] += 1


def print_all_sections(measurements, swatch_data):
    m1 = 0
    m2 = 0
    x = 0
    i_d = True
    stitch_height = swatch_data['stitch_height']
    stitch_width = swatch_data['stitch_width']
    rows = 0
    row_count = [0]
    last_row = 0
    for i in range(3):
        m1 = measurements['bodice_widths'][i]
        print(m1)
        m2 = measurements['bodice_widths'][i+1]
        print(m2)
        x = measurements['section_heights'][i]
        rows = int(x // stitch_height)
        stitches = quadratics.put_it_all_together_horizontal(m1, m2, x, stitch_height, rows, stitch_width, i_d)
        print(stitches)
        if i == 0:
            print(f'Foundation ch {stitches["row 0"]}')
        print_section(stitches, swatch_data['stitch_type'], row_count)
        if m2 - m1 > 0:
            i_d = True
        else:
            i_d = False
        if i == 2:
            last_row = stitches.popitem()
    return last_row

def calculate_f_and_b_inc(increase):
    increase_data = {
        'front_increase': 0,
        'back_decrease': 0
    }

    total_stitches = increase

    while total_stitches > 0:
        if total_stitches % 2 == 0:
            increase_data['front_increase'] += 1
            
        else:
            increase_data['back_increase'] += 1
        
            total_stitches -= 1


#OLD CODE

# def calculate_repeat(rows, rows_between):
#     num_repeats = rows // rows_between

#     return num_repeats

# def calculate_remaining_rows(rows, rows_between, repeat):
#     remaining_rows = rows - (rows_between * (repeat))
    
#     return remaining_rows


# this can definetely be reduced to one function with different calls
# turned it into two functions instead works better now 

# def print_rows_increase(rows, rows_between, num_increases, stitch):
#     row_counter = 2
#     increase = False
#     increase_counter = 0

#     while row_counter < rows:
#         if (row_counter + 1) > rows or (row_counter + rows_between + 1) > rows:
#             rows_between = int((rows - row_counter) / (num_increases - increase_counter))
#             if increase == False:
#                 print_regular_repeat(row_counter, rows_between, stitch)
#                 row_counter += (rows_between)
#                 increase = True
#             else:
#                 row_counter += 1
#                 print_increase(row_counter, stitch)
#                 row_counter += 1
#                 increase_counter += 1
#                 increase = False
#         else: 
#             if increase == False:
#                 print_regular_repeat(row_counter, rows_between, stitch)
#                 row_counter += (rows_between)
#                 increase = True
#             else:
#                 row_counter += 1
#                 print_increase(row_counter, stitch)
#                 row_counter += 1
#                 increase_counter += 1
#                 increase = False

    # print_data = {
    #     'row_counter': row_counter
    # }

    # return print_data

# we might not need this with the print_decrease function
# def print_rows_decrease(rows, rows_between, num_decreases, stitch): 

 
            

