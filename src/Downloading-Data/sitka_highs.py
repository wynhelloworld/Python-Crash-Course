from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('./weather_data/sitka_weather_2014.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 打印出列表题和下标, 看日期和最低/最高温度的下标
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
# 得出, 日期0   最高温度1   最低温度2

# 提取日期、最高温度
dates = []
highs = []
for row in reader:
    date = datetime.strptime(row[0], '%Y-%m-%d')
    high = int(row[1])
    dates.append(date)
    highs.append(high)

# 绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

ax.set_title("Daily High Temperatures, 2014", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()