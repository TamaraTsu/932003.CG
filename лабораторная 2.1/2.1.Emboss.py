import cv2
import numpy as np

# Загрузка изображения
image_path = r'C:\Users\LENOVO\Desktop\ayato.png'
image = cv2.imread(image_path)

# Проверка, успешно ли загружено изображение
if image is None:
    print(f"Error: Unable to load the image from {image_path}")
else:
    # Определите ядро для эффекта тиснения
    kernel_emboss = np.array([[0, 1, 0],
                             [1, 0, -1],
                             [0, -1, 0]])

    # Примените свертку с помощью функции filter2D из OpenCV
    embossed_image = cv2.filter2D(image, -1, kernel_emboss)
    embossed_image = cv2.add(embossed_image, 128)


    # Отобразите оригинал и эффект эмбосса
    cv2.imshow('Original', image)
    cv2.imshow('Embossed', embossed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
