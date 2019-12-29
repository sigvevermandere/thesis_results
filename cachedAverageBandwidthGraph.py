import json, matplotlib.pyplot as plt
import matplotlib
plt.style.use('science')
data = {}


def open_file(name):
    with open(name) as file:
        return json.load(file)


data['rawAvgMin_ts'] = open_file('testData/cachedData/onRawDataAvgMin_timestamps.txt')
data['summariesAvgMin_ts'] = open_file('testData/cachedData/summariesWeekAvgMinData_timestamps.txt')
data['rawAvgMin'] = open_file('testData/cachedData/onRawDataAvgMin.txt')
data['summariesAvgMin'] = open_file('testData/cachedData/summariesWeekAvgMinData.txt')

# add extra element so raw and summary graphs are equally long
data['summariesAvgMin_ts'].append(data['rawAvgMin_ts'][-1])
data['summariesAvgMin'].append(data['summariesAvgMin'][-1])

data['rawAvgHour_ts'] = open_file('testData/cachedData/onRawDataAvgHour_timestamps.txt')
data['summariesAvgHour_ts'] = open_file('testData/cachedData/summariesWeekAvgHourData_timestamps.txt')
data['rawAvgHour'] = open_file('testData/cachedData/onRawDataAvgHour.txt')
data['summariesAvgHour'] = open_file('testData/cachedData/summariesWeekAvgHourData.txt')

# add extra element so raw and summary graphs are equally long
data['summariesAvgHour_ts'].append(data['rawAvgHour_ts'][-1])
data['summariesAvgHour'].append(data['summariesAvgHour'][-1])

data['rawAvgDay_ts'] = open_file('testData/cachedData/onRawDataAvgDay_timestamps.txt')
data['summariesAvgDay_ts'] = open_file('testData/cachedData/summariesWeekAvgDayData_timestamps.txt')
data['rawAvgDay'] = open_file('testData/cachedData/onRawDataAvgDay.txt')
data['summariesAvgDay'] = open_file('testData/cachedData/summariesWeekAvgDayData.txt')

# add extra element so raw and summary graphs are equally long
data['summariesAvgDay_ts'].append(data['rawAvgDay_ts'][-1])
data['summariesAvgDay'].append(data['summariesAvgDay'][-1])

raw_answers = range(len(data['rawAvgMin_ts']))
summaries_answers = list(raw_answers) + [raw_answers[-1]]
plt.rc('axes', labelsize=12)
fig, axs = plt.subplots(3, 1)
st = fig.suptitle("Bandwidth usage comparison between server side\n and client side average summaries for cached fragments", fontsize="x-large")

axs[0].plot(data['rawAvgMin_ts'], data['rawAvgMin'], label="Client Side")
axs[0].plot(data['summariesAvgMin_ts'], data['summariesAvgMin'], label="Server Side")
axs[0].legend(loc="upper left")
axs[0].set_title('Average per minute')
axs[0].set_xlabel('Milliseconds')
axs[0].set_ylabel('Data')

axs[1].plot(data['rawAvgHour_ts'], data['rawAvgHour'], label="Client Side")
axs[1].plot(data['summariesAvgHour_ts'], data['summariesAvgHour'], label="Server Side")
axs[1].legend(loc="upper left")
axs[1].set_title('Average per hour')
axs[1].set_xlabel('Milliseconds')
axs[1].set_ylabel('Data')

axs[2].plot(data['rawAvgDay_ts'], data['rawAvgDay'], label="Client Side")
axs[2].plot(data['summariesAvgDay_ts'], data['summariesAvgDay'], label="Server Side")
axs[2].legend(loc="upper left")
axs[2].set_title('Average per day')
axs[2].set_xlabel('Milliseconds')
axs[2].set_ylabel('Data')


# lgd = fig.legend(loc="center right",   # Position of legend
#                 prop={'size': 12}
#                 )

fig.set_tight_layout(True)
# plt.suptitle("Bandwidth usage comparison between server side and client side summaries")
fig.set_size_inches(4, 9)
fig.canvas.draw()
fig.set_tight_layout(False)
st.set_y(0.95)
fig.subplots_adjust(top=0.86)

# fig.set_size_inches(4, 12)
# fig.set_tight_layout(True)
#fig.show()
plt.savefig("cachedAverageBandwidth.png", dpi=100)


