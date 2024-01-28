import cv2
import numpy as np

def apply_blur(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Проверка
    if image is None:
        print(f"Error: Unable to load the image from {image_path}")
        return

    #Ядро
    blur_kernel_matrix = np.array([[1, 1, 1],
                                   [1, 5, 1],
                                   [1, 1, 1]], dtype=np.float32) /13  # 3x3 averaging kernel


    # Применение эффекта
    blurred_image = cv2.filter2D(image, -1, blur_kernel_matrix)

    # Окна
    cv2.imshow('Original', image)
    cv2.imshow('Blurred', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Путь к изображению
    image_path = r'C:\Users\LENOVO\Desktop\ayato.png'

    # Применяем эффект
    apply_blur(image_path)


