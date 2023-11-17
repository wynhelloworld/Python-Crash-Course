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

## 制作全球地震散点图: GeoJSON 格式

```python
from pathlib import Path
import json
import plotly.express as px
import pandas as pd

path = Path('./eq_data/all_eq_20231017-12231111.geojson')
try:
    contents = path.read_text()  # Windows系统默认是unicode, 所以会出现UnicodeDecodeError异常
except:
    contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)  # 将json转换成dict

path = Path('eq_data/readable_eq_data.geojson')
readable_eq_data = json.dumps(all_eq_data, indent=4)  # 将dict转换成json
path.write_text(readable_eq_data)  # 将json写入文件中

all_eq_dicts = all_eq_data['features']  # 取到所有的地震特征
mags = []  # 震级
titles = []  # 标题
lons = []  # 经度
lats = []  # 纬度
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    if mag < 0:  # 下面画图时, 发现震级居然有负数, 所以这里做一下特殊处理
        mag = 0
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级'])

fig = px.scatter(
    # x=lons,
    # y=lats,
    # labels={'x': '经度', 'y': '纬度'},
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',  # 根据震级划分点的大小
    size_max=10,  # 限制点的大小最大为10
    color='震级',  # 根据震级划分颜色
    hover_name='位置', # 显示地震发生位置
)
# fig.write_html('global_earthquakes.html')
fig.show()
```

