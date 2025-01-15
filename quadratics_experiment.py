#c in the bodice section is how far into the body it pushes the curve at x = 0. this is for the increase and the main difference is that we subtract m1 from m2 and divide it by two. for example an increase will happen between the waist and the hip. if we drew a line straight down from the bust the c measurement is going to be the difference between the waist and the bust / 2 for each side. 
def find_c_inc(m1, m2):
    c = (m1 - m2) / 2

    return c


#The reason we subtract m1 from m2 on the decrease is similar logic to the find_c_inc. The printing bodice algorithm will start at a wider measurement like the hip and move inward towards a smaller measurement at the waist. we know c will be the difference if it is curved inward / 2
def find_c_dec(m1, m2):
    c = (m2 - m1) / 2

    return c

# ^^ a problem with the above assumptions is the math is in a 2d space and not a 3d one. I believe most yarns will be flexible enough to accomadate this issue but if enough people bring it up as an issue then we can add some more to the ease


# this is where the signs of the functions get weird. So if we remember from the find_c_inc it should return a -c value. 
def find_a_inc(c, length):
    a = (-c / (-(length ** 2)))

    return a

def find_a_dec(c, length):
    a = (-c / (length ** 2))

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


