import measurements
import stitch_swatch_data

def define_sleeve_variables(swatch_data, measurements):
    sleeve_variables = {}

    sleeve_variables['sleeve_cap_rows'] = int(measurements['arm hole depth'] / swatch_data['stitch_height'])
    sleeve_variables['sleeve_rows'] = int((measurements['sleeve length'] / swatch_data['stitch_height']) - sleeve_variables['sleeve_cap_rows'])

    sleeve_variables['sleeve_stitches_at_top'] = int((measurements['upper arm circ'] + 1) * swatch_data['row_gauge'])
    sleeve_variables['sleeve_cap_top_stitches'] = sleeve_variables['sleeve_stitches_at_top'] // 2

    sleeve_variables['stitches_at_wrist'] = int((measurements['wrist'] + 1) * swatch_data['stitch_width'])

    sleeve_variables['sleeve_total_increase'] = sleeve_variables['sleeve_stitches_at_top'] - sleeve_variables['stitches_at_wrist']
    sleeve_variables['sleeve_stitch_increase'] = 2
    sleeve_variables['sleeve_rows_between_increase'] = int((sleeve_variables['sleeve_rows'] / (sleeve_variables['sleeve_total_increase'] / sleeve_variables['sleeve_stitch_increase'])))

    sleeve_variables['sleeve_cap_total_decrease'] = sleeve_variables['sleeve_stitches_at_top'] - sleeve_variables['sleeve_cap_top_stitches']
    sleeve_variables['sleeve_cap_rows_between_decrease'] = sleeve_variables['sleeve_cap_rows'] // sleeve_variables['sleeve_cap_total_decrease']
    sleeve_variables['sleeve_cap_stitch_decrease'] = 2

    return sleeve_variables

# print(define_sleeve_variables(get_swatch_data))