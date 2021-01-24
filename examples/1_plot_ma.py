import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from backtest_function import GetHistoryData
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--date", default="20180903", type=str, help="Date")
parser.add_argument("--stockid", default="3008", type=str, help="Stock ID")
parser.add_argument("--cycle", default=60, type=int, help="The cycle of MA (second)")
parser.add_argument("--ma_len", default=10, type=int, help="The interval of MA = cycle * ma_len (second)")
args = parser.parse_args()

data = GetHistoryData(args.date, args.stockid)

MAarray = []
MA_time = []
MA_value = []
init_time = datetime.datetime.strptime('090000000000', "%H%M%S%f")
cycle = args.cycle
ma_len = args.ma_len

for i in data:
    time = datetime.datetime.strptime(i[0], "%H%M%S%f")
    price = float(i[2])
    if len(MAarray) == 0:
        MAarray.append(price)
    else:
        if time < init_time + datetime.timedelta(0, cycle):
            MAarray[-1] = price
        else:
            if len(MAarray) == ma_len:
                MAarray = MAarray[1:] + [price]
            else:
                MAarray.append(price)   
            init_time += datetime.timedelta(0, cycle)
    val = float(sum(MAarray))/len(MAarray)
    MA_value.append(val)
    MA_time.append(mdates.date2num(time))    

# line graph
sTime = [datetime.datetime.strptime(line[0], "%H%M%S%f") for line in data]
nTime = [mdates.date2num(line) for line in sTime]
price = [float(line[2]) for line in data]

# plot
plt.figure("Price and MA")             
ax = plt.subplot(111)
ax.plot_date(nTime, price, 'k-')
ax.plot_date(MA_time, MA_value, 'r-')
hfmt = mdates.DateFormatter("%H:%M")
ax.xaxis.set_major_formatter(hfmt)
plt.show()
