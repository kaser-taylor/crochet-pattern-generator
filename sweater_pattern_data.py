import measurements
import stitch_swatch_data

def define_sleeve_variables():
    sleeve_variables = {}

    sleeve_variables['sleeve_cap_rows'] = int(measurements.user_measurements['arm hole depth'] * stitch_swatch_data.get_swatch_data()['row_gauge'])
    sleeve_variables['sleeve_rows'] = int((measurements.user_measurements['sleeve length'] * stitch_swatch_data.get_swatch_data()['row_gauge']) - sleeve_variables['sleeve_cap_rows'])

    sleeve_variables['sleeve_stitches_at_top'] = int((measurements.user_measurements['upper arm circ'] + 1) * stitch_swatch_data.get_swatch_data()['row_gauge'])
    sleeve_variables['sleeve_cap_top_stitches'] = sleeve_variables['sleeve_stitches_at_top'] // 2

    sleeve_variables['stitches_at_wrist'] = int((measurements.user_measurements['wrist'] + 1) * stitch_swatch_data.get_swatch_data()['row_gauge'])

    sleeve_variables['sleeve_total_increase'] = sleeve_variables['sleeve_stitches_at_top'] - sleeve_variables['stitches_at_wrist']
    sleeve_variables['sleeve_rows_between_increase'] = sleeve_variables['sleeve_rows'] // sleeve_variables['sleeve_total_increase']
    sleeve_variables['sleeve_stitch_increase'] = 2

    sleeve_variables['sleeve_cap_total_decrease'] = sleeve_variables['sleeve_stitches_at_top'] - sleeve_variables['sleeve_cap_top_stitches']
    sleeve_variables['sleeve_cap_rows_between_decrease'] = sleeve_variables['sleeve_cap_rows'] // sleeve_variables['sleeve_cap_total_decrease']
    sleeve_variables['sleeve_cap_stitch_decrease'] = 2

    return sleeve_variables