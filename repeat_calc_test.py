rows = 12
rows_between = 3

def calculate_repeat(rows, rows_between):
    num_repeats = rows // rows_between

    return num_repeats

def calculate_remaining_rows(rows, rows_between):
    remaining_rows = rows % (rows // rows_between)
    
    return remaining_rows
    
def print_regular_repeat(row_counter, regular_repeat):
    print(f'Row {row_counter} - {row_counter + regular_repeat} sc', '/n')

def print_increase(row_counter):
    print(f'Row {row_counter} 2sc in first st 2sc in last')

def print_rows(rows, rows_between, remaing_rows):
    repeat = rows // rows_between
    row_counter = 2
    while row_counter < rows - remaing_rows:
        if row_counter % repeat == 0:
            print_increase(row_counter)
            row_counter += 1
        elif rows - row_counter == remaing_rows:
            print(f'Sc {row_counter} - {rows}')
        else:  
            print_regular_repeat(row_counter, repeat)
            row_counter += rows_between

print_rows(rows, rows_between, calculate_remaining_rows(rows, rows_between))

# print_rows(rows, calculate_repeat(rows, rows_between), calculate_remaining_rows(rows, rows_between))

# def print_rows(row_data, rows):
#     row_counter = 2
#     # for i in range(0, rows, row_data[1]):
#     #     print(f'Row {row_counter}-{row_counter + row_data[0]} sc', '\n')
#     #     print(f'Row {row_counter + row_data[1]} 2sc in first st 2sc in last')
#     #     row_counter += (row_data[1])
#     while row_counter <= rows - row_data[2]:
#         print(f'Row {row_counter}-{row_counter + row_data[0]} sc', '\n')
#         print(row_counter)
#         print(f'Row {row_counter + row_data[1]} 2sc in first st 2sc in last')
#         row_counter += 1
#         print(row_counter)
#         row_counter += (row_data[1])
        
#     if rows - row_counter == row_data[2]:
#         print(f'Row {row_counter}-{rows} sc')
    

# print(calculate_repeat(rows, rows_between))
# print_rows(calculate_repeat(rows, rows_between), rows)
