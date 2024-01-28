import cv2
import numpy as np

def apply_image_filter(image_path, kernel):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print(f"Error: Unable to load the image from {image_path}")
        return

    # Get image dimensions
    height, width, _ = image.shape

    # Get kernel size
    N = len(kernel)
    
    # Check if the image has sufficient size for the kernel
    if height < N or width < N:
        print("Error: Image size is too small for the specified kernel.")
        return

    # Normalize the kernel
    kernel_sum = np.sum(kernel)
    if kernel_sum != 0:
        kernel = kernel / kernel_sum

    # Create an array for the filtered image
    filtered_image = np.zeros_like(image, dtype=np.uint8)

    # Iterate over pixels in the image
    for i in range(1 + N // 2, height - 1):
        for j in range(1 + N // 2, width - 1):
            sum_channels = [0, 0, 0]
            for k1 in range(i - N // 2, i + N // 2 + 1):
                for k2 in range(j - N // 2, j + N // 2 + 1):
                    # Ensure indices are within bounds
                    if 0 <= k1 < height and 0 <= k2 < width:
                        clr = image[k1, k2]
                        sum_channels[0] += clr[0] * kernel[k1 - (i - N // 2)][k2 - (j - N // 2)]
                        sum_channels[1] += clr[1] * kernel[k1 - (i - N // 2)][k2 - (j - N // 2)]
                        sum_channels[2] += clr[2] * kernel[k1 - (i - N // 2)][k2 - (j - N // 2)]


            # Assign the filtered value to the corresponding pixel in the result image
            for c in range(3):
                sum_channels[c] = max(0, min(sum_channels[c], 255))
                sum_channels[c] = round(sum_channels[c])
                filtered_image[i, j, c] = sum_channels[c]

    # Display the original and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Filtered Image', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage
    custom_kernel = np.array([[1, 1, 1],
                             [1, 1, 1],
                             [1, 1, 1]])

    image_path = r'C:\Users\LENOVO\Desktop\cat.jpg'
    apply_image_filter(image_path, custom_kernel)
