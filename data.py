from dataclasses import dataclass

@dataclass
class Measurements:
    bust: float
    high_chest: float
    body_length: float
    sleeve_length: float
    shoulder_width: float
    arm_hole_depth: float
    waist: float
    hip: float
    hip_to_waist: float
    waist_to_bust: float
    bust_to_neckline: float
    wrist: float
    neck: float
    upper_arm_circ: float

# Creating instances for each size
s = Measurements(
    bust=35,
    high_chest=31.5,
    body_length=23,
    sleeve_length=22,
    shoulder_width=14.5,
    arm_hole_depth=7.5,
    waist=31,
    hip=35,
    hip_to_waist=8.5,
    waist_to_bust=8.75,
    bust_to_neckline=6.5,
    wrist=6.25,
    neck=19,
    upper_arm_circ=11.5,
)

m = Measurements(
    bust=39,
    high_chest=34.5,
    body_length=24,
    sleeve_length=23,
    shoulder_width=15.5,
    arm_hole_depth=8.5,
    waist=33,
    hip=39,
    hip_to_waist=9,
    waist_to_bust=9.25,
    bust_to_neckline=7,
    wrist=6.65,
    neck=21,
    upper_arm_circ=13,
)

l = Measurements(
    bust=43,
    high_chest=37.5,
    body_length=25,
    sleeve_length=24,
    shoulder_width=16.5,
    arm_hole_depth=9.5,
    waist=37,
    hip=43,
    hip_to_waist=9.5,
    waist_to_bust=9.75,
    bust_to_neckline=7.5,
    wrist=7.25,
    neck=23,
    upper_arm_circ=14.5,
)

xl = Measurements(
    bust=47,
    high_chest=44.6,
    body_length=26,
    sleeve_length=25,
    shoulder_width=17.5,
    arm_hole_depth=10.5,
    waist=41,
    hip=47,
    hip_to_waist=10,
    waist_to_bust=10.25,
    bust_to_neckline=8,
    wrist=7.75,
    neck=25,
    upper_arm_circ=16,
)

xxl = Measurements(
    bust=51,
    high_chest=48.5,
    body_length=27,
    sleeve_length=26,
    shoulder_width=18.5,
    arm_hole_depth=11.5,
    waist=45,
    hip=51,
    hip_to_waist=10.5,
    waist_to_bust=10.75,
    bust_to_neckline=8.5,
    wrist=8.25,
    neck=27,
    upper_arm_circ=17.5,
)

@dataclass
class StitchType:
    name: str
    height: int
    description: str

# Example list of stitch types based on your data
stitch_types = [
    StitchType(name='sc', height=1, description='Single crochet'),
    StitchType(name='hdc', height=2, description='Half double crochet'),
    StitchType(name='dc', height=3, description='Double crochet'),
    StitchType(name='tr', height=4, description='Treble crochet'),
    StitchType(name='dtr', height=5, description='Double treble crochet'),
    StitchType(name='trtr', height=6, description='Triple treble crochet'),
    StitchType(name='fpdc', height=3, description='Front post double crochet'),
    StitchType(name='bpdc', height=3, description='Back post double crochet'),
    StitchType(name='fptr', height=4, description='Front post treble crochet'),
    StitchType(name='bptr', height=4, description='Back post treble crochet'),
    StitchType(name='pc', height=3, description='Popcorn stitch (typically requires the height of a double crochet)'),
    StitchType(name='sh', height=3, description='Shell stitch (typically follows the height of double crochet)'),
    StitchType(name='cl', height=3, description='Cluster stitch (usually follows the height of double crochet)'),
    StitchType(name='v-st', height=3, description='V-stitch (usually the height of double crochet)'),
    StitchType(name='puff', height=1, description='Puff stitch (varies depending on height)'),
    StitchType(name='bob', height=3, description='Bobble stitch (usually similar to double crochet height)'),
    StitchType(name='sp st', height=1, description='Spike stitch (same as single crochet)'),
]

class CrochetStitch:
    name: str
    abbreviation: str

# Example list of crochet stitches based on your data
crochet_stitches = [
    CrochetStitch(name="chain", abbreviation="ch"),
    CrochetStitch(name="slip stitch", abbreviation="sl st"),
    CrochetStitch(name="single crochet", abbreviation="sc"),
    CrochetStitch(name="half double crochet", abbreviation="hdc"),
    CrochetStitch(name="double crochet", abbreviation="dc"),
    CrochetStitch(name="treble crochet", abbreviation="tr"),
    CrochetStitch(name="double treble crochet", abbreviation="dtr"),
    CrochetStitch(name="triple treble crochet", abbreviation="trtr"),
    CrochetStitch(name="front post double crochet", abbreviation="fpdc"),
    CrochetStitch(name="back post double crochet", abbreviation="bpdc"),
    CrochetStitch(name="front post treble crochet", abbreviation="fptr"),
    CrochetStitch(name="back post treble crochet", abbreviation="bptr"),
    CrochetStitch(name="increase", abbreviation="inc"),
    CrochetStitch(name="decrease", abbreviation="dec"),
    CrochetStitch(name="popcorn stitch", abbreviation="pc"),
    CrochetStitch(name="shell stitch", abbreviation="sh"),
    CrochetStitch(name="cluster stitch", abbreviation="cl"),
    CrochetStitch(name="v-stitch", abbreviation="v-st"),
    CrochetStitch(name="puff stitch", abbreviation="puff"),
    CrochetStitch(name="bobble stitch", abbreviation="bob"),
    CrochetStitch(name="spike stitch", abbreviation="sp st"),
]

