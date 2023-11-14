import random


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
