import print_rows

tracking_data = {
    'stitch_count': 100,
    'row_counter': 5
        }

decrease_data = {
    'row 0 - 1': -2,
    'row 1 - 2': -1,
    'row 2 - 3': -1, 
    'row 3 - 4': -1, 
    'row 4 - 5': -1, 
    'row 5 - 6': -2, 
    'row 6 - 7': -2, 
    'row 7 - 8': -2, 
    'row 8 - 9': -2
    }

print(print_rows.print_sleeve_cap(tracking_data, decrease_data, 'double crochet'))
