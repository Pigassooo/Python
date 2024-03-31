import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# 数据
x_train = np.array([1.0, 1.7, 2.0, 2.5, 3.0, 3.5])
y_train = np.array([250, 300, 480, 430, 630, 730])

# 计算成本函数
def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost_sum = np.sum(((w * x + b) - y) ** 2)
    total_cost = (1 / (2 * m)) * cost_sum
    return total_cost

# 最小二乘法拟合线性回归
def fit_linear_regression(x, y):
    w = np.dot((x - np.mean(x)), (y - np.mean(y))) / np.dot((x - np.mean(x)), (x - np.mean(x)))
    b = np.mean(y) - w * np.mean(x)
    return w, b

# 生成w和b的网格
W = np.linspace(-300, 500, 100)
B = np.linspace(-300, 300, 100)
W, B = np.meshgrid(W, B)
costs = np.array([compute_cost(x_train, y_train, w, b) for w, b in zip(np.ravel(W), np.ravel(B))])
Z = costs.reshape(W.shape)

# 创建图表布局
fig = plt.figure(figsize=(18, 8))

# 左边 - 线性回归图
ax1 = fig.add_subplot(121)
ax1.scatter(x_train, y_train, color='red', label='Actual Value')
w, b = fit_linear_regression(x_train, y_train)
y_pred = w * x_train + b
ax1.plot(x_train, y_pred, color='blue', label='Our Prediction')
for xi, yi, yp in zip(x_train, y_train, y_pred):
    ax1.plot([xi, xi], [yi, yp], color='gray', linestyle='--', linewidth=1)
ax1.set_xlabel('Size (1000 sqft)')
ax1.set_ylabel('Price (in 1000s of dollars)')
ax1.set_title('Housing Prices')
ax1.legend()

# 右边上部 - 成本函数等高线图
ax2 = fig.add_subplot(222)
contour = ax2.contour(W, B, Z, levels=30, cmap=cm.viridis)
ax2.clabel(contour, inline=1, fontsize=10)
ax2.set_xlabel('w')
ax2.set_ylabel('b')
ax2.set_title('Cost(w,b)')

# 右边下部 - 3D 成本表面图
ax3 = fig.add_subplot(224, projection='3d')
surf = ax3.plot_surface(W, B, Z, cmap=cm.viridis, alpha=0.8)
fig.colorbar(surf, ax=ax3, shrink=0.5, aspect=5)
ax3.set_xlabel('w')
ax3.set_ylabel('b')
ax3.set_zlabel('Cost')
ax3.set_title('Cost(w,b) [You can rotate this figure]')

plt.tight_layout()
plt.show()
