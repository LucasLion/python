from load_image import ft_load
from PIL import Image


def zoom(path):
    img_array = ft_load(path)
    zoomed_image_array = img_array[100:500, 450:950, :1]
    print("New shape after slicing:",
          zoomed_image_array.shape,
          "or",
          zoomed_image_array.shape[:2])

    zoomed_image_array_img = Image.fromarray(zoomed_image_array.squeeze())
    zoomed_image_array_img.save('zoom.jpg')


def main(path: str):
    zoom(path)


if __name__ == "__main__":
    main('animal.jpeg')
