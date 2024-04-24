from load_image import ft_load

from PIL import Image


def zoom(path, x, y, width, height):
    img_array = ft_load(path)
    zoomed_image_array = img_array[y:height, x:width, :1]
    print('-----------')
    print(zoomed_image_array)
    print('-----------')
    print("New shape after slicing:",
          zoomed_image_array.shape,
          "or",
          zoomed_image_array.shape[:2])

    print(zoomed_image_array)
    zoomed_image_array_img = Image.fromarray(zoomed_image_array.squeeze())
    zoomed_image_array_img.save('zoom.jpg')
    print('Nouvelle image enregistree sous zoom.jpg')


def main(path: str):
    x = 450
    y = 100
    width = x + 400
    height = y + 400
    zoom(path, x, y, width, height)


if __name__ == "__main__":
    main('animal.jpeg')
