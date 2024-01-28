import cv2
import numpy as np

def apply_edge_detection(image_path, kernel):
    # Загружаем изображение в черно-белом формате
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Проверка
    if image is None:
        print(f"Error: Unable to load the image from {image_path}")
        return

    # Получаем размеры изображения
    height, width = image.shape

    # Определяем отредактированное изображение
    edge_detected_image = np.zeros_like(image, dtype=np.int32)

    # Применяем эффект
    for i in range(1, height - 1): #не обрабатываем краевые пиксели, так как не сможем сделать для них матрицу 3 x 3
        for j in range(1, width - 1):
            edge_detected_image[i, j] = np.clip(np.sum(image[i-1:i+2, j-1:j+2] * kernel), 0, 255)

    # Показываем оригинал
    cv2.imshow('Original', image)

    # Показываем результат
    cv2.imshow('Edge Detection Result', edge_detected_image.astype(np.uint8))

    # Показываем результат с противоположными цветами (черные линии на белом фоне)
    inverted_edge_detected_image = 255 - edge_detected_image
    cv2.imshow('Inverted Edge Detection Result', inverted_edge_detected_image.astype(np.uint8))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Ядро
    kernel_edge_detection = np.array([[0, 1, 0],
                                      [1, -4, 1],
                                      [0, 1, 0]])

    # Путь к изображению
    image_path =  r'C:\Users\LENOVO\Desktop\cat.jpg'

    # Применяем эффект обнаружения границ
    apply_edge_detection(image_path, kernel_edge_detection)
