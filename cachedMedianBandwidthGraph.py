import json, matplotlib.pyplot as plt
import matplotlib
plt.style.use('science')
data = {}


def open_file(name):
    with open(name) as file:
        return json.load(file)


data['rawMedianMin_ts'] = open_file('testData/cachedData/onRawDataMedianMin_timestamps.txt')
data['summariesMedianMin_ts'] = open_file('testData/cachedData/summariesWeekMedianMinData_timestamps.txt')
data['rawMedianMin'] = open_file('testData/cachedData/onRawDataMedianMin.txt')
data['summariesMedianMin'] = open_file('testData/cachedData/summariesWeekMedianMinData.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianMin_ts'].append(data['rawMedianMin_ts'][-1])
data['summariesMedianMin'].append(data['summariesMedianMin'][-1])

data['rawMedianHour_ts'] = open_file('testData/cachedData/onRawDataMedianHour_timestamps.txt')
data['summariesMedianHour_ts'] = open_file('testData/cachedData/summariesWeekMedianHourData_timestamps.txt')
data['rawMedianHour'] = open_file('testData/cachedData/onRawDataMedianHour.txt')
data['summariesMedianHour'] = open_file('testData/cachedData/summariesWeekMedianHourData.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianHour_ts'].append(data['rawMedianHour_ts'][-1])
data['summariesMedianHour'].append(data['summariesMedianHour'][-1])

data['rawMedianDay_ts'] = open_file('testData/cachedData/onRawDataMedianDay_timestamps.txt')
data['summariesMedianDay_ts'] = open_file('testData/cachedData/summariesWeekMedianDayData_timestamps.txt')
data['rawMedianDay'] = open_file('testData/cachedData/onRawDataMedianDay.txt')
data['summariesMedianDay'] = open_file('testData/cachedData/summariesWeekMedianDayData.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianDay_ts'].append(data['rawMedianDay_ts'][-1])
data['summariesMedianDay'].append(data['summariesMedianDay'][-1])

raw_answers = range(len(data['rawMedianMin_ts']))
summaries_answers = list(raw_answers) + [raw_answers[-1]]
plt.rc('axes', labelsize=12)
fig, axs = plt.subplots(3, 1)
st = fig.suptitle("Bandwidth usage comparison between server side\n and client side median summaries for cached fragments", fontsize="x-large")

axs[0].plot(data['rawMedianMin_ts'], data['rawMedianMin'], label="Client Side")
axs[0].plot(data['summariesMedianMin_ts'], data['summariesMedianMin'], label="Server Side")
axs[0].legend(loc="upper left")
axs[0].set_title('Average per minute')
axs[0].set_xlabel('Milliseconds')
axs[0].set_ylabel('Data')

axs[1].plot(data['rawMedianHour_ts'], data['rawMedianHour'], label="Client Side")
axs[1].plot(data['summariesMedianHour_ts'], data['summariesMedianHour'], label="Server Side")
axs[1].legend(loc="upper left")
axs[1].set_title('Average per hour')
axs[1].set_xlabel('Milliseconds')
axs[1].set_ylabel('Data')

axs[2].plot(data['rawMedianDay_ts'], data['rawMedianDay'], label="Client Side")
axs[2].plot(data['summariesMedianDay_ts'], data['summariesMedianDay'], label="Server Side")
axs[2].legend(loc="upper left")
axs[2].set_title('Average per day')
axs[2].set_xlabel('Milliseconds')
axs[2].set_ylabel('Data')


# lgd = fig.legend(loc="center right",   # Position of legend
#                 prop={'size': 12}
#                 )

fig.set_tight_layout(True)
# fig.canvas.draw()
# fig.set_tight_layout(False)
# plt.subplots_adjust(right=0.75)
fig.set_size_inches(4, 9)
fig.canvas.draw()
fig.set_tight_layout(False)
st.set_y(0.95)
fig.subplots_adjust(top=0.86)
#fig.show()
plt.savefig("cachedMedianBandwidth.png", dpi=100)

f = open("cachedMedianBandwidthGraph_areas.txt", "w+")
f.write("Server Side: \n")
f.write("Minute: " + str(data['summariesMedianMin'][-1]) + "\n")
f.write("Hour: " + str(data['summariesMedianHour'][-1]) + "\n")
f.write("Day: " + str(data['summariesMedianDay'][-1]) + "\n")
f.write("Client Side: \n")
f.write("Minute: " + str(data['rawMedianMin'][-1]) + "\n")
f.write("Hour: " + str(data['rawMedianHour'][-1]) + "\n")
f.write("Day: " + str(data['rawMedianDay'][-1]) + "\n")
f.close()