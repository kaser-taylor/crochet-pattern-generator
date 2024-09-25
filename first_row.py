import stitch_swatch_data

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

def print_first_row(length, stitch_type):
    ch_increment = row_start_stitch_type_int[stitch_type]
    print(f'Row 1: Ch {length + ch_increment}; {stitch_type} in {ch_increment} from hook in each ch across ')