from PIL import Image

def get_shape(path: str) -> tuple:
    img = Image.open(path)
    data = img.getdata()
    print(list(data))
    return img.size

def ft_load(path: str) -> list:
    get_shape(path)
    img = Image.open(path)
    pix = img.load()
    print(f"The shape of image is : {img.size}")
    print(pix[0, 0])
    ar = []
    print(img.size)
    return ar

ft_load("landscape.jpg")
