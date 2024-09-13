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