    
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
        if i_d == 'increase':
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
def row_tracker(rows, num_increases, rows_between, stitch, i_d='increase', stitch_count=0, row_counter=2):
    tracking_data = {
        'row_counter': row_counter,
        'increase': False,
        'increase_counter': 0,
        'stitch_count': stitch_count
    }

    while tracking_data['row_counter'] < rows:
        if (tracking_data['row_counter']) >= rows or (tracking_data['row_counter'] + rows_between) >= rows:
            final_rows_between = int((rows - tracking_data['row_counter']) / (num_increases - tracking_data['increase_counter']))
            print_rows(tracking_data, final_rows_between, stitch, i_d)
            break
        else:
            print_rows(tracking_data, rows_between, stitch, i_d)
    
    while num_increases != tracking_data['increase_counter']:
        final_rows_between = int((rows - tracking_data['row_counter']) / (num_increases - tracking_data['increase_counter']))
        print_rows(tracking_data, rows_between, stitch, i_d)
    
    return tracking_data


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

 
            

