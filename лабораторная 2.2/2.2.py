import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Переменные
points_src = []  # Точки на оригинальном изображении
points_dst = []  # Точки на target изображени
image = None
target = None

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def load_images(image_path):
    global image, target
    image = cv2.imread(image_path)
    target = image.copy()  # target - копия оригинального изображения
    cv2.imshow('Original Image', image)
    cv2.imshow('Target Image', target)

def mouse_click(event, x, y, flags, param):
    global points_src, points_dst, image, target

    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points_src) < 3:
            points_src.append((x, y))
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1) #ставим 3 точки
            cv2.imshow('Original Image', image)
        elif len(points_dst) < 3:
            points_dst.append((x, y))
            cv2.circle(target, (x, y), 5, (255, 0, 0), -1)
            cv2.imshow('Target Image', target)

        if len(points_src) == 3 and len(points_dst) == 3:
            choose_transformation_method()

def choose_transformation_method():
    global points_src, points_dst, image, target

    root = tk.Tk()
    root.title("Choose Transformation Method")

    def apply_simple():
        result = apply_transformation(points_src, points_dst, cv2.INTER_NEAREST)
        cv2.imshow('Transformed Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def apply_bilinear():
        result = apply_transformation(points_src, points_dst, cv2.INTER_LINEAR)
        cv2.imshow('Transformed Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Дальше код для того, чтобы окна были на экране
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 300
    window_height = 100
    window_x = (screen_width - window_width) // 2
    window_y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    #оформление окна выбора алгоритма
    simple_button = tk.Button(root, text="Simple Algorithm", command=apply_simple)
    simple_button.pack(side=tk.LEFT, padx=10)

    bilinear_button = tk.Button(root, text="Bilinear Interpolation", command=apply_bilinear)
    bilinear_button.pack(side=tk.RIGHT, padx=10)

    root.mainloop()
#трансформация
def apply_transformation(src_points, dst_points, interpolation):
    M = cv2.getAffineTransform(np.float32(src_points), np.float32(dst_points))
    transformed = cv2.warpAffine(image, M, (target.shape[1], target.shape[0]), flags=interpolation)
    return transformed

image_path = open_file_dialog()

if image_path:
    load_images(image_path)
    cv2.setMouseCallback('Original Image', mouse_click)
    cv2.setMouseCallback('Target Image', mouse_click)
    cv2.waitKey(0)
