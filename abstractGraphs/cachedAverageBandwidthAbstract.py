import json, matplotlib.pyplot as plt
import matplotlib
plt.style.use('science')
data = {}


def open_file(name):
    with open(name) as file:
        return json.load(file)

data['rawAvgHour_ts'] = open_file('../testData/cachedData/onRawDataAvgHour_timestamps.txt')
data['summariesAvgHour_ts'] = open_file('../testData/cachedData/summariesWeekAvgHourData_timestamps.txt')
data['rawAvgHour'] = open_file('../testData/cachedData/onRawDataAvgHour.txt')
data['summariesAvgHour'] = open_file('../testData/cachedData/summariesWeekAvgHourData.txt')

# add extra element so raw and summary graphs are equally long
data['summariesAvgHour_ts'].append(data['rawAvgHour_ts'][-1])
data['summariesAvgHour'].append(data['summariesAvgHour'][-1])

plt.rc('axes', labelsize=12)
fig = plt.figure()
axes = fig.add_subplot(1,1,1)
st = fig.suptitle("Bandwidth usage comparison between server side\n and client side hourly average summaries\n for cached fragments", fontsize="x-large")

axes.plot(data['rawAvgHour_ts'], data['rawAvgHour'], label="Client Side")
axes.plot(data['summariesAvgHour_ts'], data['summariesAvgHour'], label="Server Side")
axes.legend(loc="upper left")
axes.set_xlabel('Milliseconds')
axes.set_ylabel('Data')

fig.set_tight_layout(True)
# plt.suptitle("Bandwidth usage comparison between server side and client side summaries")
fig.set_size_inches(5, 4)
fig.canvas.draw()
fig.set_tight_layout(False)
st.set_y(0.95)
fig.subplots_adjust(top=0.8)
# plt.tight_layout()
plt.savefig("cachedAverageBandwidthAbstract.png", dpi=100)


