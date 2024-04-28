from load_image import ft_load
from PIL import Image
import numpy as np


def rotate(path: str):
    array_image = ft_load(path)
    zoomed_image_array = array_image[200:600, 450:850, :1]
    img = np.zeros((zoomed_image_array.shape[1], zoomed_image_array.shape[0]), dtype=np.uint8)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            img[x, y] = zoomed_image_array[y, x]
    zoomed_image_array_horizontal = img.squeeze()
    zoomed_image_array_img = Image.fromarray(zoomed_image_array_horizontal)
    zoomed_image_array_img.save('zoom.jpg')
    print("The shape of the image is",
          zoomed_image_array.shape,
          "or",
          zoomed_image_array.shape[:2])
    print(zoomed_image_array)
    print("New shape after Transpose:",
          img.shape[:2])
    print(zoomed_image_array_horizontal)


def main(path: str):
    rotate(path)


if __name__ == "__main__":
    main('animal.jpeg')
