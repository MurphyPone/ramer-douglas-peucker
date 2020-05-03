import math
from vector import *
import matplotlib.pyplot as plt
import numpy as np

def n_map(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2


def get_target_line():
    all_points = []
    width, height = 800, 600
    for x in range(width):
        xval = n_map(x, 0, width, 0, 5)
        yval = math.exp(-xval) * math.cos(2*math.pi * xval)
        y = n_map(yval, -1, 1, height, 0)
        all_points.append(Vector(x,y))

    return list(all_points)

# finds the index of the furthest element in points between indices a, b
def find_furthest(points, a, b, ε):
    record_distance = -1
    furthest = -1
    start = points[a]
    end = points[b]
    for i in range(a+1, b):
        current = points[i]
        d = dist_from_line(current, start, end)
        if(d > record_distance):
            record_distance = d
            furthest = i

    if record_distance > ε:
        return furthest
    else:
        return -1


def rdp(startIndex, endIndex, allPoints, rdpPoints, ε):
    nextIndex = find_furthest(allPoints, startIndex, endIndex, ε)
    if(nextIndex > 0):
        if(startIndex != nextIndex):
            rdp(startIndex, nextIndex, allPoints, rdpPoints, ε)
        
        rdpPoints.append(allPoints[nextIndex])
        
        if(nextIndex != endIndex):
            rdp(nextIndex, endIndex, allPoints, rdpPoints, ε)