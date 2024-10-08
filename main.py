import measurements
import stitch_swatch_data
import sweater_pattern_data
import print_rows
import first_row

def main():
    #gets user size
    default_size = measurements.get_size()

    #gets default measurements from user size
    default_measurements = measurements.get_measurements(default_size)

    #gets user adjusments 
    final_measurements = measurements.user_adjustments(default_measurements)

    #gets swatch data from user and calculates data from that
    swatch_data = stitch_swatch_data.get_swatch_data()

    #sleeve_data
    sleeve_data = sweater_pattern_data.define_sleeve_variables(swatch_data, final_measurements)
    print(sleeve_data)

    #prints first row of sleeve
    first_row.print_first_row(sleeve_data['stitches_at_wrist'], swatch_data['stitch_type'], swatch_data['stitch_gauge'])

    #prints sleeve
    print_sleeve_data = print_rows.print_rows_increase(sleeve_data['sleeve_rows'], sleeve_data['sleeve_rows_between_increase'], sleeve_data['sleeve_total_num_increases'], swatch_data['stitch_type'])
    
    #prints first row of sleeve cap
    sleeve_cap_first_row_data = first_row.print_first_row_new_section(print_sleeve_data['row_counter'], swatch_data['stitch_type'])

if __name__ == '__main__':
    main()