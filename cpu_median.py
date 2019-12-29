import json, matplotlib.pyplot as plt
import dateutil.parser
import matplotlib
plt.style.use('science')
data = {}


def open_file(name):
    with open(name) as file:
        json_file = json.load(file)
        x = []
        y = []
        offset_time = dateutil.parser.parse(json_file[0]["time"]).timestamp() * 1000
        offset_value = json_file[0]["value"]
        for el in json_file:
            x_val = dateutil.parser.parse(el["time"]).timestamp() * 1000 - offset_time
            x.append(x_val)
            y_val = el["value"] - offset_value
            y.append(y_val)
        stop = False
        counter = 1
        last_val = y[-counter]
        while not stop:
            if y[-counter] != last_val:
                stop = True
            else:
                counter += 1
        if -counter + 3 < 0:
            x = x[:-counter + 3]
            y = y[:-counter + 3]
        return x, y

data['rawMedian_aqs1'] = open_file('testData/cpuData/onRawDataAvgMin_aqs1_cpu.txt')
data['rawMedian_aqs2'] = open_file('testData/cpuData/onRawDataAvgMin_aqs2_cpu.txt')

data['summariesMedianMin_aqs1'] = open_file('testData/cpuData/summariesWeekMedianMinData_aqs1_cpu.txt')
data['summariesMedianMin_aqs2'] = open_file('testData/cpuData/summariesWeekMedianMinData_aqs2_cpu.txt')

data['summariesMedianHour_aqs1'] = open_file('testData/cpuData/summariesWeekMedianHourData_aqs1_cpu.txt')
data['summariesMedianHour_aqs2'] = open_file('testData/cpuData/summariesWeekMedianHourData_aqs2_cpu.txt')

# data['summariesMedianDay_aqs1'] = open_file('testData/cpuData/summariesWeekMedianDayData_aqs1_cpu.txt')
# data['summariesMedianDay_aqs2'] = open_file('testData/cpuData/summariesWeekMedianDayData_aqs2_cpu.txt')

plt.rc('axes', labelsize=14)
fig, axs = plt.subplots(2, 1)

axs[0].plot(data['rawMedian_aqs1'][0], data['rawMedian_aqs1'][1], label="Client Side node 1")
axs[0].plot(data['rawMedian_aqs2'][0], data['rawMedian_aqs2'][1], label="Client Side node 2")
axs[0].plot(data['summariesMedianMin_aqs1'][0], data['summariesMedianMin_aqs1'][1], label="Server Side node 1")
axs[0].plot(data['summariesMedianMin_aqs2'][0], data['summariesMedianMin_aqs2'][1], label="Server Side node 2")
axs[0].legend(loc="upper left")
axs[0].set_title('Median per minute: CPU', fontsize=16)
axs[0].set_xlabel('Milliseconds')
axs[0].set_ylabel('CPU tasks')

axs[1].plot(data['rawMedian_aqs1'][0], data['rawMedian_aqs1'][1], label="Client Side node 1")
axs[1].plot(data['rawMedian_aqs2'][0], data['rawMedian_aqs2'][1], label="Client Side node 2")
axs[1].plot(data['summariesMedianHour_aqs1'][0], data['summariesMedianHour_aqs1'][1], label="Server Side node 1")
axs[1].plot(data['summariesMedianHour_aqs2'][0], data['summariesMedianHour_aqs2'][1], label="Server Side node 2")
axs[1].legend(loc="upper left")
axs[1].set_title('Median per hour: CPU', fontsize=16)
axs[1].set_xlabel('Milliseconds')
axs[1].set_ylabel('CPU tasks')

# lgd = fig.legend(loc="center right",   # Position of legend
#                 prop={'size': 14}
#                 )
#
# fig.set_tight_layout(True)
# fig.canvas.draw()
# fig.set_tight_layout(False)
# plt.subplots_adjust(right=0.75)
fig.set_size_inches(8, 10)

plt.savefig("cpu_median.png", dpi=100)