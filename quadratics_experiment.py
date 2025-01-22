#THIS IS ALL GARBAGE HAVE TO REWRITE ALGO BECAUSE THIS CHANGES THE C VALUE FOR EVERY PASS THROUGH PLEASE LOOK AT DESMOS WHEN YOU WRITE STUFF SO YOU DONT WAIST A MILLION HOURS
def find_c_inc(m1, m2):
    c = (m2 - m1) / 2

    return c
def find_c_dec(m1, m2):
    c = (m1 - m2) / 2

    return c

# ^^ a problem with the above assumptions is the math is in a 2d space and not a 3d one. I believe most yarns will be flexible enough to accomadate this issue but if enough people bring it up as an issue then we can add some more to the ease


# this is where the signs of the functions get weird. So if we remember from the find_c_inc it should return a -c value. a is the slope of the parabola and on an increase in stitches we actually want a  
def find_a_inc(c, length):
    a = (-c / (length ** 2))

    return a

def find_a_dec(c, length):
    a = (-c / (-(length ** 2)))

    return a

def find_y_inc(a, length, i, stitch_height, c):
    length = length + (i * stitch_height)
    y = (a * (-(length ** 2))) + c

    return y

def find_y_dec(a, length, i, stitch_height, c):
    length = 0 + (i * stitch_height)
    y = (a * (length ** 2)) + c

    return y

def find_rows(length, stitch_height):
    rows = length / stitch_height

    return rows


