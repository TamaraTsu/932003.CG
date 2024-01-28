import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию для расчета кубической кривой Безье
def cubic_bezier(p0, p1, p2, p3, t):
    """ Возвращает точку на кубической кривой Безье. """
    return ((1 - t) ** 3) * p0 + 3 * t * ((1 - t) ** 2) * p1 + 3 * (t ** 2) * (1 - t) * p2 + (t ** 3) * p3

# Опорные точки
points = np.array([(2, 6),(1, -3),(-5, -4),(-4, 1),(5,0)])



# Расчет контрольных точек для крайних сегментов
# Для простоты, предположим, что контрольные точки лежат на прямых, соединяющих соседние опорные точки
p0, p1, p2, p3,p4 = points
# Контрольные точки для первого сегмента
p01 = p0 + 2/3 * (p1 - p0)
p02 = p1 - 1/3 * (p2 - p0)
# Контрольные точки для второго сегмента
p11 = p1 + 1/3 * (p2 - p0)
p12 = p2 - 1/3 * (p3 - p1)
# Контрольные точки для третьего сегмента
p21 = p2 + 1/3 * (p3 - p1)
p22 = p3 - 2/3 * (p3 - p2)

p31 = p3 + 1/3 * (p4 - p1)
p32 = p4 - 2/3 * (p4 - p2)

# Строим кривую Безье
t = np.linspace(0, 1, 100)
curve1 = np.array([cubic_bezier(p0, p01, p02, p1, t_i) for t_i in t])
curve2 = np.array([cubic_bezier(p1, p11, p12, p2, t_i) for t_i in t])
curve3 = np.array([cubic_bezier(p2, p21, p22, p3, t_i) for t_i in t])
curve4 = np.array([cubic_bezier(p3, p31, p32, p4, t_i) for t_i in t])



# Визуализация
plt.figure(figsize=(8, 6))
plt.plot(curve1[:, 0], curve1[:, 1], 'r')
plt.plot(curve2[:, 0], curve2[:, 1], 'g')
plt.plot(curve3[:, 0], curve3[:, 1], 'b')
plt.plot(curve4[:, 0], curve4[:, 1], 'y')
plt.scatter(points[:, 0], points[:, 1], color='black')
plt.title("Кубические кривые Безье")
plt.xlabel("X")
plt.ylabel("Y")
# Отображение контрольных точек
plt.scatter([p0[0], p01[0], p02[0], p1[0]], [p0[1], p01[1], p02[1], p1[1]], color='red', marker='*')
plt.scatter([p1[0], p11[0], p12[0], p2[0]], [p1[1], p11[1], p12[1], p2[1]], color='green', marker='*')
plt.scatter([p2[0], p21[0], p22[0], p3[0]], [p2[1], p21[1], p22[1], p3[1]], color='blue', marker='*')



plt.grid(True)
plt.show()
