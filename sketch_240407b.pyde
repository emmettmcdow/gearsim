from __future__ import division

DIGITAL_COG = True
DIGITAL_CR = True

def setup():
    size(1000, 1000)
    strokeWeight(3)
    colorMode(HSB)
    
    
def draw():
    background(75)
    # settings
    origin = (width/2, height/2)
    rpm = 15
    rpms = rpm / 60000.0 # 1m = 60s = 60,000ms
    chainring_teeth = 5
    chainring_pos = (origin[0] + 200, origin[1])
    cog_teeth = 2
    cog_pos = (origin[0] - 200, origin[1])

    time_ms = millis()
    
    # Chainring spin
    # 1 r = 360deg
    # ms * r/ms = ms
    offset_deg_cr = time_ms * rpms * 360
    
    # Gear speed
    cog_rpms = (chainring_teeth / cog_teeth) * rpms
    offset_deg_cog = time_ms * cog_rpms * 360
    
    # If we want integer movement
    if (DIGITAL_CR):
        offset_deg_cr = floor(offset_deg_cr / (360 / chainring_teeth)) * (360 / chainring_teeth)
    if (DIGITAL_COG):
        offset_deg_cog = floor(offset_deg_cog / (360 / cog_teeth)) * (360 / cog_teeth)

    # Chainring
    gear(chainring_teeth, chainring_pos, offset_deg_cr, 200)

    # Cog
    gear(cog_teeth, cog_pos, offset_deg_cog, 100)

def gear(teeth_n, origin, starting_theta, spoke_len):
    offset_theta = 360 / teeth_n

    # Start from starting_theta
    top_x = dest_x = origin[0]
    top_y = dest_y = origin[1] + spoke_len
    top = (top_x, top_y)
    top = rotate_line(top, origin, starting_theta)
    
    origin = (origin[0], origin[1])
    for tooth_i in range(teeth_n):
        curr_theta = tooth_i * offset_theta

        stroke(curr_theta/2, 360, 360)
        dest_x, dest_y = rotate_line(top, origin, curr_theta)

        line(origin[0],
             origin[1],
             dest_x,
             dest_y)

def rotate_line_x(pnt, origin, theta):
    t_x = pnt[0] - origin[0]
    t_y = pnt[1] - origin[1]
    res = t_x * cos(radians(theta)) - t_y * sin(radians(theta))
    return res + origin[0]

def rotate_line_y(pnt, origin, theta):
    t_x = pnt[0] - origin[0]
    t_y = pnt[1] - origin[1]
    res = t_y * cos(radians(theta)) + t_x * sin(radians(theta))
    return res + origin[1]

def rotate_line(pnt, origin, theta):
    return (rotate_line_x(pnt, origin, theta),
            rotate_line_y(pnt, origin, theta))
