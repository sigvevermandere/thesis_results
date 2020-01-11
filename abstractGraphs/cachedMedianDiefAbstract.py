import json, matplotlib.pyplot as plt
from matplotlib.patches import Polygon
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


data['rawMedianMin_ts'] = open_file('../testData/cachedData/onRawDataMedianMin_dief.txt')
data['summariesMedianMin_ts'] = open_file('../testData/cachedData/summariesWeekMedianMinData_dief.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianMin_ts'].append(data['rawMedianMin_ts'][-1])

data['rawMedianHour_ts'] = open_file('../testData/cachedData/onRawDataMedianHour_dief.txt')
data['summariesMedianHour_ts'] = open_file('../testData/cachedData/summariesWeekMedianHourData_dief.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianHour_ts'].append(data['rawMedianHour_ts'][-1])

raw_answers = range(len(data['rawMedianMin_ts']))
summaries_answers = list(raw_answers) + [raw_answers[-1]]
plt.rc('axes', labelsize=12)
fig = plt.figure()
axes = fig.add_subplot(1,1,1)
st = fig.suptitle("Diefficiency comparison between server side\n and client side hourly median summaries for cached fragments", fontsize="x-large")


axes.plot(data['rawMedianHour_ts'], raw_answers, label="Client Side")
axes.plot(data['summariesMedianHour_ts'], summaries_answers, label="Server Side")
axes.legend(loc="upper left")
axes.set_xlabel('Milliseconds')
axes.set_ylabel('Answers')

poly = get_poly(data['rawMedianHour_ts'], raw_answers)
pts = poly.get_path().vertices
clientside_area_hour = PolyArea(pts[:,0], pts[:,1])

poly = get_poly(data['summariesMedianHour_ts'], summaries_answers)
pts = poly.get_path().vertices
serverside_area_hour = PolyArea(pts[:,0], pts[:,1])

fig.set_tight_layout(True)
# fig.canvas.draw()
# fig.set_tight_layout(False)
# plt.subplots_adjust(right=0.8)

fig.set_size_inches(5, 4)
fig.canvas.draw()
fig.set_tight_layout(False)
st.set_y(0.95)
fig.subplots_adjust(top=0.8)

#fig.show()
plt.savefig("cachedMedianDiefAbstract.png", dpi=100)


f = open("cachedMedianDiefAbstract_areas.txt", "w+")
f.write("Server Side: \n")
f.write("Hour: " + str(serverside_area_hour) + "\n")
f.write("Client Side: \n")
f.write("Hour: " + str(clientside_area_hour) + "\n")
f.close()