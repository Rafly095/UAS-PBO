import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        self.blurred_img = None

    def apply_gaussian_blur(self, kernel_size=(15, 15), resize_factor=0.5):
        # Mengubah resolusi gambar 
        resized_img = cv2.resize(self.img, None, fx=resize_factor, fy=resize_factor)

        # Mengaplikasikan Gaussian Blur 
        self.blurred_img = cv2.GaussianBlur(resized_img, kernel_size, 0)

    def show_image(self, window_name='Blurred Image'):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        # Menyesuaikan ukuran jendela 
        cv2.resizeWindow(window_name, self.blurred_img.shape[1], self.blurred_img.shape[0])

        if self.blurred_img is not None:
            cv2.imshow(window_name, self.blurred_img)
        else:
            print("Error: Gaussian blur not applied. Call apply_gaussian_blur() first.")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Contoh penggunaan
if __name__ == "__main__":
    image_processor = ImageProcessor('GoYoonJung.jpeg')
    image_processor.apply_gaussian_blur(resize_factor=0.5)

    # Menampilkan
    image_processor.show_image('Blurred Image')
