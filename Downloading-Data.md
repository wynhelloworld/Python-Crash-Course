## CSV 文件格式

```python
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('./weather_data/death_valley_2014.csv')
lines = path.read_text().splitlines()  # 以方式读取上面文件, 并且按行分开 (每行都是一个列表, 列表中的每个元素都是字符串)

reader = csv.reader(lines)  # 以csv方式解析读取到的文件
header_row = next(reader)  # 返回reader里的第一行(在这里就是标题行), next会永久移动reader里的迭代器

# 打印出列表题和下标, 看日期和最低/最高温度的下标
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
# 得出, 日期0   最高温度1   最低温度2

# 提取日期、最高温度、最低温度
dates = []
highs = []
lows = []
for row in reader:
    date = datetime.strptime(row[0], '%Y-%m-%d')
    try:
        high = int(row[1])
        low = int(row[2])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

# 绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)  # alpha 设置透明度(0全透明, 1不透明)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # 填充highs与lows之间的区域的颜色为蓝色

ax.set_title("Daily High Temperatures, July 2014", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()  # 使x轴标签倾斜
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)  

plt.show()
```