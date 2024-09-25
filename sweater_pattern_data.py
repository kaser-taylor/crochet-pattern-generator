import measurements

def define_sleeve_variables(swatch_data):
    sleeve_variables = {}

    sleeve_variables['sleeve_cap_rows'] = int(measurements.final_measurements['arm hole depth'] * swatch_data['row_gauge'])
    sleeve_variables['sleeve_rows'] = int((measurements.final_measurements['sleeve length'] * swatch_data['row_gauge']) - sleeve_variables['sleeve_cap_rows'])

    sleeve_variables['sleeve_stitches_at_top'] = int((measurements.final_measurements['upper arm circ'] + 1) * swatch_data['row_gauge'])
    sleeve_variables['sleeve_cap_top_stitches'] = sleeve_variables['sleeve_stitches_at_top'] // 2

    sleeve_variables['stitches_at_wrist'] = int((measurements.final_measurements['wrist'] + 1) * swatch_data['row_gauge'])

    sleeve_variables['sleeve_total_increase'] = sleeve_variables['sleeve_stitches_at_top'] - sleeve_variables['stitches_at_wrist']
    sleeve_variables['sleeve_rows_between_increase'] = sleeve_variables['sleeve_rows'] // sleeve_variables['sleeve_total_increase']
    sleeve_variables['sleeve_stitch_increase'] = 2

    sleeve_variables['sleeve_cap_total_decrease'] = sleeve_variables['sleeve_stitches_at_top'] - sleeve_variables['sleeve_cap_top_stitches']
    sleeve_variables['sleeve_cap_rows_between_decrease'] = sleeve_variables['sleeve_cap_rows'] // sleeve_variables['sleeve_cap_total_decrease']
    sleeve_variables['sleeve_cap_stitch_decrease'] = 2

    return sleeve_variables