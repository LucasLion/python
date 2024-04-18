from load_image import ft_load
from PIL import Image


def zoom(img):
    zoomed_image_array = img[450:850, 200:600, :1]
#    print("The shape of the image is", 
#          zoomed_image_array.shape, 
#          "or", 
#          zoomed_image_array.shape[:2])
#
    print(zoomed_image_array)
    zoomed_image_array_img = Image.fromarray(zoomed_image_array.squeeze())
    zoomed_image_array_img.save('zoom.jpg')
    return zoomed_image_array_img


def rotate(path: str):
    array_image = ft_load(path)

    t = array_image.transpose((1, 0, 2))
    print("The shape of the image is", 
          t.shape, 
          "or", 
          t.shape[:2])
    image = zoom(t)
    image.save('t.jpg')


def main(path: str):
    rotate(path)


if __name__ == "__main__":
    main('animal.jpeg')
