import math
from vector import *
from util import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

ε = 0
all_points = get_target_line()

ax = plt.axes()
x_t = [v.x for v in all_points]
y_t = [v.y for v in all_points]


rdp_points = []

total = len(all_points)
start = all_points[0]
end = all_points[total-1]
rdp_points.append(start)
rdp(0, total-1, all_points, rdp_points, ε)
rdp_points.append(end)

ε += 0.01
if(ε > 100):
    ε = 0

x_rdp = [v.x for v in rdp_points]
y_rdp = [v.y for v in rdp_points]

ax.plot(x_t, y_t)
ax.plot(x_rdp, y_rdp)
plt.show()










