import matplotlib.pyplot as plt
from random_walk import RandomWalk


# 死循环, 模拟多次随机游走
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=224)  # 参数用来调整尺寸以适应屏幕, 我的mac电脑的api是224
    point_numbers = range(rw.num_points)  # 用来进行颜色映射, edgecolors 参数用来删除每个点的轮廓
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, edgecolors='none', s=1)

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
