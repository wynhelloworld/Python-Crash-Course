## 安装Matplotlib

```python
python3 -m pip install --user matplotlib
```

- `python3 -m ` 用于指定在 python3 环境下安装
- `--user` 用于将包安装到用户主目录下

## 绘制简单的折线图

```pyth
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
```

- `fig` 全称 figure, 意思是 `subplots` 函数创建了一个画板 
- `ax` 全称 axes, 意思是 `subplots` 函数在 `fig` 上创建了一个笛卡尔坐标系. 之后对于图像的绘制, 一般都使用该对象
- `plot` 意思是绘图, 当传入一个列表参数时, 可以理解为传入了坐标系中的 y 轴的各点, 此时 x 轴默认从 0 开始(极易导致绘图不准确)

#### 修改标签文字和线条粗细

```python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# 设置图的标题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=24)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()
```

#### 矫正绘图

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()
```

- 在**绘制简单的折线图**处, 说了, 当 `plot` 函数只传入一个列表参数时, 该参数被认为是 y 轴上的点, 而 x 轴上的点默认从 0 开始, 所以为了矫正绘图的不准确, 可以同时传入 x 和 y

#### 使用内置样式

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()
```

- 在调用 `subplots` 函数生成画板和笛卡尔坐标系之前, 调用 `plt.style.use` 函数即可使用内置样式. 书中说 `seaborn` 样式会出现警告, 不会影响运行, 但我进行实验时, 会出现 OSError, 运行中断
- 通过打印 `plt.style.available` 可以得到所有内置样式

#### 使用 scatter() 绘制散点图并设置样式

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(2, 4)

plt.show()
```

- 通过调用 `scatter` 函数, 可以画点. 在本例中, 画了一个点, 坐标为 (2, 4)

#### 使用 scatter() 绘制一系列点

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.scatter(x, y, s=100)

plt.show()
```

- 在本例中, 画了五个点. s 参数指定了点的大小.

#### 自动计算数据

```python
import matplotlib.pyplot as plt

x = range(1, 1001)
y = [i**2 for i in x]

fig, ax = plt.subplots()
ax.scatter(x, y, s=10)
ax.axis([0, 1100, 0, 1_100_000])

plt.show()
```

-  通过函数和列表推导式, 可以快速生成数据 x 和 y
- 通过调用 `axis` 函数, 可以指定每个坐标轴的取值范围, [0, 1100] 是 x 轴的取值范围, [0, 1100000] 是 y 轴的取值范围

#### 定制刻度标记

```python
import matplotlib.pyplot as plt

x = range(1, 1001)
y = [i**2 for i in x]

fig, ax = plt.subplots()
ax.scatter(x, y, s=10)
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()
```

- 在刻度标记表示的数足够大时, Matplotlib 默认使用科学记数法, 通过调用 `ticklabel_format` 函数, 可以覆盖默认的刻度标记样式

#### 定制颜色

```python
import matplotlib.pyplot as plt

x = range(1, 1001)
y = [i**2 for i in x]

fig, ax = plt.subplots()
# ax.scatter(x, y, color='red', s=10)
ax.scatter(x, y, color=(0, 0.8, 0), s=10)
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()
```

- `scatter` 函数的 `color` 参数可以定制点的颜色, 可以选择传入指定参数, 也可以选择传入 RGB 参数

#### 使用颜色映射

```python
import matplotlib.pyplot as plt

x = range(1, 1001)
y = [i**2 for i in x]

fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()
```

- `scatter` 函数的 `c` 参数设置成了 y, 并使用参数 `cmap` 告诉 pyplot 使用蓝色映射, 最终会导致, y 坐标值较小的点显示为浅蓝色, y 坐标值较大的点, 显示为深蓝色 

#### 自动保存绘图

```python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.savefig('name.png', bbox_inches='tight')
```

- `show` 函数会将图片显示到 Matplotlib 查看器上, 而 `savefig` 函数会将图片命名成 name.png, 然后保存到相对路径上, `bbox_inches` 参数会切割掉图片周围多余的部分, 若不想切割, 则忽略掉该参数即可

## 随机游走

```python
import random
import matplotlib.pyplot as plt


'''
创建一个RandomWalk类, 该类需要三个属性:
    一个是跟踪随机游走次数的变量,
    另外两个是列表, 分别存储随机游走经过的每个点的x坐标值和y坐标值
'''
class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # 分别计算出下个随机点相对的水平方向及距离和竖直轴方向及距离,
            x_direction = random.choice([-1, 1])
            x_distance = random.choice([0, 1, 2, 3, 4, 5])
            x_step = x_direction * x_distance

            y_direction = random.choice([-1, 1])
            y_distance = random.choice([0, 1, 2, 3, 4, 5])
            y_step = y_direction * y_distance

            # 下个随机点不能原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 根据坐标列表中最后一个点的坐标, 计算出下个随机点的真实坐标
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # 将下个随机点的真实坐标尾插入坐标列表中
            self.x_values.append(x)
            self.y_values.append(y)


# 死循环, 模拟多次随机游走
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=224) # 参数用来调整尺寸以适应屏幕, 我的mac电脑的api是224
    point_numbers = range(rw.num_points) # 用来进行颜色映射, edgecolors 参数用来删除每个点的轮廓
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 指定两条轴上刻度的间距必须相等
    ax.set_aspect('equal')

    # 重新绘制起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

```



<script src="https://giscus.app/client.js"
        data-repo="wynhelloworld/blog-comments"
        data-repo-id="R_kgDOKruZpg"
        data-category="Announcements"
        data-category-id="DIC_kwDOKruZps4Ca2L0"
        data-mapping="url"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        crossorigin="anonymous"
        async>
</script>

本站所有文章转发 **CSDN** 将按侵权追究法律责任，其它情况随意。

