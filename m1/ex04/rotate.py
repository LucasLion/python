from load_image import ft_load
from PIL import Image


def rotate(path: str):
    array_image = ft_load(path)
    zoomed_image_array = array_image[200:600, 450:850, :1]
    zoomed_image_array_transpose = zoomed_image_array.transpose((1, 0, 2))
    zoomed_image_array_horizontal = zoomed_image_array_transpose.squeeze()
    zoomed_image_array_img = Image.fromarray(zoomed_image_array_horizontal)
    zoomed_image_array_img.save('zoom.jpg')
    print("The shape of the image is", 
          zoomed_image_array.shape, 
          "or", 
          zoomed_image_array.shape[:2])
    print(zoomed_image_array)
    print("New shape after Transpose:",
          zoomed_image_array_transpose.shape[:2])
    print(zoomed_image_array_horizontal)


def main(path: str):
    rotate(path)


if __name__ == "__main__":
    main('animal.jpeg')
