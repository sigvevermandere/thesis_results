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

data['rawMedian_aqs1'] = open_file('../testData/cpuData/onRawDataAvgMin_aqs1_cpu.txt')
data['rawMedian_aqs2'] = open_file('../testData/cpuData/onRawDataAvgMin_aqs2_cpu.txt')

data['summariesMedianHour_aqs1'] = open_file('../testData/cpuData/summariesWeekMedianHourData_aqs1_cpu.txt')
data['summariesMedianHour_aqs2'] = open_file('../testData/cpuData/summariesWeekMedianHourData_aqs2_cpu.txt')

# data['summariesMedianDay_aqs1'] = open_file('testData/cpuData/summariesWeekMedianDayData_aqs1_cpu.txt')
# data['summariesMedianDay_aqs2'] = open_file('testData/cpuData/summariesWeekMedianDayData_aqs2_cpu.txt')

plt.rc('axes', labelsize=12)
fig = plt.figure()
axes = fig.add_subplot(1,1,1)
st = fig.suptitle("CPU usage comparison between server side\n and client side hourly median summaries", fontsize="x-large")


axes.plot(data['rawMedian_aqs1'][0], data['rawMedian_aqs1'][1], label="Client Side: node 1")
axes.plot(data['rawMedian_aqs2'][0], data['rawMedian_aqs2'][1], label="Client Side: node 2")
axes.plot(data['summariesMedianHour_aqs1'][0], data['summariesMedianHour_aqs1'][1], label="Server Side: node 1")
axes.plot(data['summariesMedianHour_aqs2'][0], data['summariesMedianHour_aqs2'][1], label="Server Side: node 2")
axes.legend(loc="upper left")
axes.set_xlabel('Milliseconds')
axes.set_ylabel('CPU tasks')

fig.set_size_inches(5, 4)
fig.canvas.draw()
fig.set_tight_layout(False)
st.set_y(0.95)
fig.subplots_adjust(top=0.8)

plt.savefig("cpu_median_abstract.png", dpi=100)