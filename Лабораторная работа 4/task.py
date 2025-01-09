import numpy as np
import matplotlib.pyplot as plt

# Данные
KSV = np.array([1.6, 1.5, 1.67, 1.38, 1.3, 1.32, 1.45])
f = np.array([520, 540, 560, 530, 480, 470, 460])

# Квадратичная аппроксимация
coeffs = np.polyfit(f, KSV, 2)  # Коэффициенты для квадратичной аппроксимации
poly = np.poly1d(coeffs)  # Создаем полином

# Новые точки для гладкой кривой
f_new = np.linspace(min(f), max(f), 500)
KSV_new = poly(f_new)

# Строим график
plt.plot(f_new, KSV_new, label='Квадратичная аппроксимация', color='b')
plt.scatter(f, KSV, color='red', label='Исходные точки')

# Подписываем оси
plt.xlabel("Частота (MHz)")
plt.ylabel("КСВ")

# Легенда и сетка
plt.legend()
plt.grid(True)

# Показать график
plt.show()
