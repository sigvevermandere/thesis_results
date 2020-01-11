import json, matplotlib.pyplot as plt
import matplotlib
plt.style.use('science')
data = {}


def open_file(name):
    with open(name) as file:
        return json.load(file)

data['rawMedianHour_ts'] = open_file('../testData/cachedData/onRawDataMedianHour_timestamps.txt')
data['summariesMedianHour_ts'] = open_file('../testData/cachedData/summariesWeekMedianHourData_timestamps.txt')
data['rawMedianHour'] = open_file('../testData/cachedData/onRawDataMedianHour.txt')
data['summariesMedianHour'] = open_file('../testData/cachedData/summariesWeekMedianHourData.txt')

# add extra element so raw and summary graphs are equally long
data['summariesMedianHour_ts'].append(data['rawMedianHour_ts'][-1])
data['summariesMedianHour'].append(data['summariesMedianHour'][-1])

plt.rc('axes', labelsize=12)
fig = plt.figure()
axes = fig.add_subplot(1,1,1)
st = fig.suptitle("Bandwidth usage comparison between server side\n and client side hourly median summaries for cached fragments", fontsize="x-large")

axes.plot(data['rawMedianHour_ts'], data['rawMedianHour'], label="Client Side")
axes.plot(data['summariesMedianHour_ts'], data['summariesMedianHour'], label="Server Side")
axes.legend(loc="upper left")
axes.set_title('Average per hour')
axes.set_xlabel('Milliseconds')
axes.set_ylabel('Data')



# lgd = fig.legend(loc="center right",   # Position of legend
#                 prop={'size': 12}
#                 )

fig.set_tight_layout(True)
# fig.canvas.draw()
# fig.set_tight_layout(False)
# plt.subplots_adjust(right=0.75)
fig.set_size_inches(5, 4)
fig.canvas.draw()
fig.set_tight_layout(False)
st.set_y(0.95)
fig.subplots_adjust(top=0.8)
#fig.show()
plt.savefig("cachedMedianBandwidthAbstract.png", dpi=100)
