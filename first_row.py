import stitch_swatch_data


# the number of initial stitches it takes to start a row eg. a single crochet needs one extra, a dc needs three extra
row_start_stitch_type_int = {
    'sc': 1,            # Single crochet
    'hdc': 2,           # Half double crochet
    'dc': 3,            # Double crochet
    'tr': 4,            # Treble crochet
    'dtr': 5,           # Double treble crochet
    'trtr': 6,          # Triple treble crochet
    'fpdc': 3,          # Front post double crochet
    'bpdc': 3,          # Back post double crochet
    'fptr': 4,          # Front post treble crochet
    'bptr': 4,          # Back post treble crochet
    'pc': 3,            # Popcorn stitch (typically requires the height of a double crochet)
    'sh': 3,            # Shell stitch (typically follows the height of double crochet)
    'cl': 3,            # Cluster stitch (usually follows the height of double crochet)
    'v-st': 3,          # V-stitch (usually the height of double crochet)
    'puff': 1,          # Puff stitch (varies depending on height)
    'bob': 3,           # Bobble stitch (usually similar to double crochet height)
    'sp st': 1          # Spike stitch (same as single crochet)
}

#takes in the length, stitch type, and stitch gauge. ch increment is set to the stitch type of the patter. then the first row is printed based on the length and stitch gauge.
def print_first_row(length, stitch_type, stitch_gauge):
    
    ch_increment = row_start_stitch_type_int[stitch_type]
    print(f'Row 1: Ch {int((length / stitch_gauge) + ch_increment)}; {stitch_type} in {ch_increment} from hook in each ch across ')

#takes in the row and stitch type and prints the first row of a new section. this can be useful when multiple sections are crocheted in one go
def print_first_row_new_section(row, stitch_type):
    print(f'Row {row}: {stitch_type}')
    return row

#prints the chain for the bodice section. could use something like the print_first_row where it takes in the stitch type and adds it to the chain length
def print_first_bodice_ch(stitches_per_row):
    print(f'Foundation ch {stitches_per_row["row 0"]}')