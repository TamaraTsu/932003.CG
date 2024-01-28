import cv2
import numpy as np

# Загрузка изображения
image_path = r'C:\Users\LENOVO\Desktop\ayato.png'
image = cv2.imread(image_path)

# Проверка, успешно ли загружено изображение
if image is None:
    print(f"Error: Unable to load the image from {image_path}")
else:
    # Определите ядро для эффекта увеличения резкости
    kernel_emboss = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])

    # Примените свертку с помощью функции filter2D из OpenCV
    sharpened_image = cv2.filter2D(image, -1, kernel_emboss)

    # Отобразите оригинал и эффект эмбосса
    cv2.imshow('Original', image)
    cv2.imshow('Sharpened', sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
