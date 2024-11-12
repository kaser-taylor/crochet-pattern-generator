import measurements
import quadratics
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

    #gets desired fit
    baggy_factor = measurements.define_baggy_factor()

    #adjusts measurements to desired fit
    processed_measurements = measurements.processed_measurements(final_measurements, baggy_factor)
    print(processed_measurements)

    #gets swatch data from user and calculates data from that
    swatch_data = stitch_swatch_data.get_swatch_data()

    #sleeve_data
    sleeve_data = sweater_pattern_data.define_sleeve_variables(swatch_data, processed_measurements)
    print(sleeve_data)

    #prints first row of sleeve
    first_row.print_first_row(processed_measurements['wrist'], swatch_data['stitch_type'], swatch_data['stitch_width'])

    #prints sleeve

    # print_sleeve_data = print_rows.print_rows_increase(sleeve_data['sleeve_rows'], sleeve_data['sleeve_rows_between_increase'], sleeve_data['sleeve_total_num_increases'], swatch_data['stitch_type'])
    print_sleeve_data = print_rows.row_tracker(sleeve_data['sleeve_rows'], sleeve_data['sleeve_total_num_increases'], sleeve_data['sleeve_rows_between_increase'], swatch_data['stitch_type'])

    #gets sleeve cap decreases
    decreases = quadratics.put_it_all_together(processed_measurements['upper arm circ'], processed_measurements['arm hole depth'], swatch_data['stitch_height'], sleeve_data['sleeve_cap_rows'], swatch_data['stitch_width'])
    print(decreases)

    #prints first row of sleeve cap
    sleeve_cap_first_row_data = first_row.print_first_row_new_section(print_sleeve_data['row_counter'], swatch_data['stitch_type'])

    #prints sleeve cap
    sleeve_cap = print_rows.print_sleeve_cap(print_sleeve_data, decreases, swatch_data['stitch_type'], sleeve_data['calculated_sleeve_stitches_at_top'])
    #test commit after making private
if __name__ == '__main__':
    main()