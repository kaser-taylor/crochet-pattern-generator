# def calculate_repeat(rows, rows_between):
#     num_repeats = rows // rows_between

#     return num_repeats

# def calculate_remaining_rows(rows, rows_between, repeat):
#     remaining_rows = rows - (rows_between * (repeat))
    
#     return remaining_rows
    
def print_regular_repeat(row_counter, rows_between, stitch):
    print(f'Row {row_counter} - {row_counter + rows_between} {stitch}')

def print_increase(row_counter, stitch):
    print(f'Row {row_counter} 2{stitch} in first st 2{stitch} in last')

def print_rows_increase(rows, rows_between, num_increases, stitch):
    row_counter = 2
    increase = False
    increase_counter = 0

    while row_counter < rows:
        if (row_counter + 1) > rows or (row_counter + rows_between + 1) > rows:
            rows_between = int((rows - row_counter) / (num_increases - increase_counter))
            if increase == False:
                print_regular_repeat(row_counter, rows_between, stitch)
                row_counter += (rows_between)
                increase = True
            else:
                row_counter += 1
                print_increase(row_counter, stitch)
                row_counter += 1
                increase_counter += 1
                increase = False
        else: 
            if increase == False:
                print_regular_repeat(row_counter, rows_between, stitch)
                row_counter += (rows_between)
                increase = True
            else:
                row_counter += 1
                print_increase(row_counter, stitch)
                row_counter += 1
                increase_counter += 1
                increase = False
    
    print_data = {
        'row_counter': row_counter
    }

    return print_data

# def print_rows_decrease {}
 
            

