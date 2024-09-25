crochet_stitches = {
    "chain": "ch",
    "slip stitch": "sl st",
    "single crochet": "sc",
    "half double crochet": "hdc",
    "double crochet": "dc",
    "treble crochet": "tr",
    "double treble crochet": "dtr",
    "triple treble crochet": "trtr",
    "front post double crochet": "fpdc",
    "back post double crochet": "bpdc",
    "front post treble crochet": "fptr",
    "back post treble crochet": "bptr",
    "increase": "inc",
    "decrease": "dec",
    "popcorn stitch": "pc",
    "shell stitch": "sh",
    "cluster stitch": "cl",
    "v-stitch": "v-st",
    "puff stitch": "puff",
    "bobble stitch": "bob",
    "spike stitch": "sp st"
}

row_start_stitch_type_str = {
    'sc': 'ch 1',            # Single crochet
    'hdc': 'ch 2',           # Half double crochet
    'dc': 'ch 3',            # Double crochet
    'tr': 'ch 4',            # Treble crochet
    'dtr': 'ch 5',           # Double treble crochet
    'trtr': 'ch 6',          # Triple treble crochet
    'fpdc': 'ch 3',          # Front post double crochet
    'bpdc': 'ch 3',          # Back post double crochet
    'fptr': 'ch 4',          # Front post treble crochet
    'bptr': 'ch 4',          # Back post treble crochet
    'pc': 'ch 3',            # Popcorn stitch (typically requires the height of a double crochet)
    'sh': 'ch 3',            # Shell stitch (typically follows the height of double crochet)
    'cl': 'ch 3',            # Cluster stitch (usually follows the height of double crochet)
    'v-st': 'ch 3',          # V-stitch (usually the height of double crochet)
    'puff': 'ch 1',          # Puff stitch (varies depending on height)
    'bob': 'ch 3',           # Bobble stitch (usually similar to double crochet height)
    'sp st': 'ch 1'          # Spike stitch (same as single crochet)
}

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

def get_width_height(swatch_size):
    dimensions = swatch_size.split('x')
    width = dimensions[0]
    height = dimensions[1]
    return (width, height)

def calc_row_gauge(height, vertical_stitch_count):
    stich_height = height / vertical_stitch_count
    return stich_height

def calc_stitch_width(width, stitch_count):
    stitch_width = width / stitch_count
    return stitch_width

def calc_stitch_gauge(width, height, vertical_stitches, horizontal_stitches):
    area = width * height
    total_stitches = vertical_stitches * horizontal_stitches
    stitches_per_inch = area // total_stitches
    return stitches_per_inch


def get_swatch_data():
    swatch_data = {}
    swatch_data['swatch_size'] = input('input the size of your swatch in this format. The first number is width, the second is height. ex. 4x4 ')
    swatch_data['vertical_stitches'] = int(input('input the number of rows in your swatch ').strip())
    swatch_data['horizontal_stitches'] = int(input('input how many stitches across your swatch is ').strip())
    swatch_data['stitch_type'] = crochet_stitches[input('input the stitch used for swatch ').strip().lower()]
    swatch_data['swatch_height'] = int(get_width_height(swatch_data['swatch_size'])[1])
    swatch_data['swatch_width']= int(get_width_height(swatch_data['swatch_size'])[0])
    swatch_data['row_gauge'] = calc_row_gauge(swatch_data['swatch_height'], swatch_data['vertical_stitches'])
    swatch_data['stitch_width'] = calc_stitch_width(swatch_data['swatch_width'], swatch_data['horizontal_stitches'])
    swatch_data['stitch_gauge'] = calc_stitch_gauge(swatch_data['swatch_width'], swatch_data['swatch_height'], swatch_data['vertical_stitches'], swatch_data['horizontal_stitches'])

    return swatch_data
