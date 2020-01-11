import json, matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from shapely.geometry import Polygon as Poly
import numpy as np
plt.style.use('science')
data = {}


def open_file(name):
    with open(name) as file:
        return json.load(file)


def get_poly(xvals, yvals):
    pts = list(zip(xvals, yvals)) + [(xvals[-1], 0)]
    return Polygon(pts, facecolor='0.9', edgecolor='0.5')

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x, np.roll(y, 1))-np.dot(y, np.roll(x, 1)))


data['rawAvgMin_ts'] = open_file('../testData/cachedData/onRawDataAvgMin_dief.txt')
data['summariesAvgMin_ts'] = open_file('../testData/cachedData/summariesWeekAvgMinData_dief.txt')

# add extra element so raw and summary graphs are equally long
data['summariesAvgMin_ts'].append(data['rawAvgMin_ts'][-1])

data['rawAvgHour_ts'] = open_file('../testData/cachedData/onRawDataAvgHour_dief.txt')
data['summariesAvgHour_ts'] = open_file('../testData/cachedData/summariesWeekAvgHourData_dief.txt')

# add extra element so raw and summary graphs are equally long
data['summariesAvgHour_ts'].append(data['rawAvgHour_ts'][-1])

data['rawAvgDay_ts'] = open_file('../testData/cachedData/onRawDataAvgDay_dief.txt')
data['summariesAvgDay_ts'] = open_file('../testData/cachedData/summariesWeekAvgDayData_dief.txt')

# add extra element so raw and summary graphs are equally long
data['summariesAvgDay_ts'].append(data['rawAvgDay_ts'][-1])

# add zero in front of each entry
for key in data:
    data[key] = [0] + data[key]

raw_answers = range(len(data['rawAvgMin_ts']))
summaries_answers = list(raw_answers) + [raw_answers[-1]]
plt.rc('axes', labelsize=12)
fig = plt.figure()
axes = fig.add_subplot(1,1,1)
st = fig.suptitle("Diefficiency comparison between server side\n and client side hourly average summaries\n for cached fragments", fontsize="x-large")


axes.plot(data['rawAvgHour_ts'], raw_answers, label="Client Side")
axes.plot(data['summariesAvgHour_ts'], summaries_answers, label="Server Side")
axes.legend(loc="upper left")
axes.set_xlabel('Milliseconds')
axes.set_ylabel('Answers')

poly = get_poly(data['rawAvgHour_ts'], raw_answers)
pts = poly.get_path().vertices
clientside_area_hour = PolyArea(pts[:,0], pts[:,1])

poly = get_poly(data['summariesAvgHour_ts'], summaries_answers)
pts = poly.get_path().vertices
serverside_area_hour = PolyArea(pts[:,0], pts[:,1])

polygon = Poly(pts)
print(polygon.area)

fig.set_tight_layout(True)
# fig.set_tight_layout(False)
# plt.subplots_adjust(right=0.8)

fig.set_size_inches(5, 4)
fig.canvas.draw()
fig.set_tight_layout(False)
st.set_y(0.95)
fig.subplots_adjust(top=0.8)

#fig.show()
plt.savefig("cachedAverageDiefAbstract.png", dpi=100)
f = open("cachedAverageDiefAbstract_areas.txt", "w+")
f.write("Server Side: \n")
f.write("Hour: " + str(serverside_area_hour) + "\n")
f.write("Client Side: \n")
f.write("Hour: " + str(clientside_area_hour) + "\n")
f.close()