# this equation finds the y value for x-intercepts. this is used to find the y values that are plugged into find_a when x = 0 THIS IS ALSO A Y VALUE PLUGGED INTO A AND THE C VALUE PLUGGED INTO FIND Y
def find_c_y(small_measure, big_measure):
    y = big_measure - small_measure
    return y

#this equation finds the slope of the parabola given two sets of x,y coordinates
def find_a(y1, y2, x1, x2):
    a = (y2 - y1) / ((x2 ** 2) - (x1 **2))

    return a

#this finds the y value on the slope this is then used to find the width at the certain place in the sweater
def find_y (a, x, c):
    y = (a(x ** 2)) + c

    return y

#finds the width given a y value
def find_width(big_measure, y):
    width = big_measure - (y * 2)

    return width

def find_stitch_num (width, stich_width):
    stitch = width // stich_width

    return stitch



