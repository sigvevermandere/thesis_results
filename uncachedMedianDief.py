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


data['rawMedianMin_ts'] = open_file('testData/uncachedData/uncached_onRawDataMedianMin_dief.txt')
data['summariesMedianMin_ts'] = open_file('testData/uncachedData/uncached_summariesWeekMedianMinData_dief.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianMin_ts'].append(data['rawMedianMin_ts'][-1])

data['rawMedianHour_ts'] = open_file('testData/uncachedData/uncached_onRawDataMedianHour_dief.txt')
data['summariesMedianHour_ts'] = open_file('testData/uncachedData/uncached_summariesWeekMedianHourData_dief.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianHour_ts'].append(data['rawMedianHour_ts'][-1])

data['rawMedianDay_ts'] = open_file('testData/uncachedData/uncached_onRawDataMedianDay_dief.txt')
data['summariesMedianDay_ts'] = open_file('testData/uncachedData/uncached_summariesWeekMedianDayData_dief.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianDay_ts'].append(data['rawMedianDay_ts'][-1])

raw_answers = range(len(data['rawMedianMin_ts']))
summaries_answers = list(raw_answers) + [raw_answers[-1]]
plt.rc('axes', labelsize=12)
fig, axs = plt.subplots(3, 2)


axs[0, 0].plot(data['rawMedianMin_ts'], raw_answers, label="Client Side")
axs[0, 0].plot(data['summariesMedianMin_ts'], summaries_answers, label="Server Side")
axs[0, 0].legend(loc="upper left")
axs[0, 0].set_title('Median per minute: dief', size=15)
axs[0, 0].set_xlabel('Milliseconds')
axs[0, 0].set_ylabel('Answers')

poly = get_poly(data['rawMedianMin_ts'], raw_answers)
pts = poly.get_path().vertices
clientside_area_min = PolyArea(pts[:,0], pts[:,1])
axs[0, 0].add_patch(poly)

axs[0, 1].plot(data['rawMedianMin_ts'], raw_answers, label="Client Side")
axs[0, 1].plot(data['summariesMedianMin_ts'], summaries_answers, label="Server Side")
axs[0, 1].legend(loc="upper left")
axs[0, 1].set_title('Median per minute: dief', size=15)
axs[0, 1].set_xlabel('Milliseconds')
axs[0, 1].set_ylabel('Answers')

poly = get_poly(data['summariesMedianMin_ts'], summaries_answers)
pts = poly.get_path().vertices
serverside_area_min = PolyArea(pts[:,0], pts[:,1])
axs[0, 1].add_patch(poly)

axs[1, 0].plot(data['rawMedianHour_ts'], raw_answers, label="Client Side")
axs[1, 0].plot(data['summariesMedianHour_ts'], summaries_answers, label="Server Side")
axs[1, 0].legend(loc="upper left")
axs[1, 0].set_title('Median per hour: dief', size=15)
axs[1, 0].set_xlabel('Milliseconds')
axs[1, 0].set_ylabel('Answers')

poly = get_poly(data['rawMedianHour_ts'], raw_answers)
pts = poly.get_path().vertices
clientside_area_hour = PolyArea(pts[:,0], pts[:,1])
axs[1, 0].add_patch(poly)

axs[1, 1].plot(data['rawMedianHour_ts'], raw_answers, label="Client Side")
axs[1, 1].plot(data['summariesMedianHour_ts'], summaries_answers, label="Server Side")
axs[1, 1].legend(loc="upper left")
axs[1, 1].set_title('Median per hour: dief', size=15)
axs[1, 1].set_xlabel('Milliseconds')
axs[1, 1].set_ylabel('Answers')

poly = get_poly(data['summariesMedianHour_ts'], summaries_answers)
pts = poly.get_path().vertices
serverside_area_hour = PolyArea(pts[:,0], pts[:,1])
axs[1, 1].add_patch(poly)

day_answers = list(range(len(data['summariesMedianDay_ts']) - 1))
day_answers.append(day_answers[-1])
axs[2, 0].plot(data['rawMedianDay_ts'], range(len(data['rawMedianDay_ts'])), label="Client Side")
axs[2, 0].plot(data['summariesMedianDay_ts'], day_answers, label="Server Side")
axs[2, 0].legend(loc="upper left")
axs[2, 0].set_title('Median per day: dief', size=15)
axs[2, 0].set_xlabel('Milliseconds')
axs[2, 0].set_ylabel('Answers')

poly = get_poly(data['rawMedianDay_ts'], range(len(data['rawMedianDay_ts'])))
pts = poly.get_path().vertices
clientside_area_day = PolyArea(pts[:,0], pts[:,1])
axs[2, 0].add_patch(poly)

axs[2, 1].plot(data['rawMedianDay_ts'], range(len(data['rawMedianDay_ts'])), label="Client Side")
axs[2, 1].plot(data['summariesMedianDay_ts'], day_answers, label="Server Side")
axs[2, 1].legend(loc="upper left")
axs[2, 1].set_title('Median per day: dief', size=15)
axs[2, 1].set_xlabel('Milliseconds')
axs[2, 1].set_ylabel('Answers')

poly = get_poly(data['summariesMedianDay_ts'], day_answers)
pts = poly.get_path().vertices
serverside_area_day = PolyArea(pts[:,0], pts[:,1])
axs[2, 1].add_patch(poly)

# lgd = fig.legend(loc="center right",   # Position of legend
#                 prop={'size': 12}
#                 )

fig.set_tight_layout(True)
# fig.canvas.draw()
# fig.set_tight_layout(False)
# plt.subplots_adjust(right=0.8)
fig.set_size_inches(8, 9)

#fig.show()
plt.savefig("uncachedMedianDief.png", dpi=100)

f = open("uncachedMedianDiefGraph_areas.txt", "w+")
f.write("Server Side: \n")
f.write("Minute: " + str(serverside_area_min) + "\n")
f.write("Hour: " + str(serverside_area_hour) + "\n")
f.write("Day: " + str(serverside_area_day) + "\n")
f.write("Client Side: \n")
f.write("Minute: " + str(clientside_area_min) + "\n")
f.write("Hour: " + str(clientside_area_hour) + "\n")
f.write("Day: " + str(clientside_area_day) + "\n")
f.close()