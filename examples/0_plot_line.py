import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from backtest_function import GetHistoryData
import pprint
import argparse


pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser()
parser.add_argument("--date", default="20180903", type=str, help="Date")
parser.add_argument("--stockid", default="3008", type=str, help="Stock ID")
args = parser.parse_args()

data = GetHistoryData(args.date, args.stockid)
print("Data: ")
pp.pprint(data[:10])

# prepare x and y
sTime = [datetime.datetime.strptime(line[0],"%H%M%S%f") for line in data]
nTime = [mdates.date2num(line) for line in sTime]
price = [float(line[2]) for line in data]

# plot
plt.figure(args.stockid)
ax = plt.subplot(1,1,1) 
plt.plot_date(nTime, price, "-")
hfmt = mdates.DateFormatter("%H:%M")
ax.xaxis.set_major_formatter(hfmt)
plt.show()
