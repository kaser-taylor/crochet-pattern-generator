def calculate_repeat(rows, rows_between):
    num_repeats = rows // rows_between

    return num_repeats

def calculate_remaining_rows(rows, rows_between, repeat):
    remaining_rows = rows - (rows_between * (repeat))
    
    return remaining_rows
    
def print_regular_repeat(row_counter, rows_between, stitch):
    print(f'Row {row_counter} - {row_counter + rows_between} {stitch}')

def print_increase(row_counter, stitch):
    print(f'Row {row_counter} 2{stitch} in first st 2{stitch} in last')

def print_rows(rows, rows_between, stitch):
    row_counter = 2
    increase = False
    increase_counter = 0

    while row_counter < rows:
        if (row_counter + 1) > rows or (row_counter + rows_between + 1) > rows:
             break
        else: 
            if increase == False:
                print_regular_repeat(row_counter, rows_between, stitch)
                row_counter += (rows_between)
                increase = True
            else:
                print_increase(row_counter, stitch)
                row_counter += 1
                increase = False
                increase_counter += 1
    else:
        print(f'Row {row_counter} - {row} ')
