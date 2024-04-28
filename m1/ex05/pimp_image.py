from array import array
import numpy as np
from PIL import Image


def ft_invert(array) -> array:
    '''
    Inverts the color of the image received.
    '''
    new_array = array.copy()
    for i in range(len(new_array)):
        for j in range(len(new_array[i])):
            for k in range(len(new_array[i][j])):
                new_array[i][j][k] = 255 - new_array[i][j][k]
    image = Image.fromarray(new_array)
    image.save("negative.jpg")
    return new_array


def ft_red(array) -> array:
    '''
    Turn the color of the image to red.
    '''
    new_array = array.copy()
    for i in range(len(new_array)):
        for j in range(len(new_array[i])):
            for k in range(len(new_array[i][j])):
                if k == 0:
                    pass
                elif k == 1 or k == 2:
                    new_array[i][j][k] = 0
    image = Image.fromarray(new_array)
    image.save("red.jpg")
    return new_array


def ft_green(array) -> array:
    '''
    Turn the color of the image to green.
    '''
    new_array = array.copy()
    for i in range(len(new_array)):
        for j in range(len(new_array[i])):
            for k in range(len(new_array[i][j])):
                if k == 1:
                    pass
                elif k == 0 or k == 2:
                    new_array[i][j][k] = 0
    image = Image.fromarray(new_array)
    image.save("green.jpg")
    return new_array


def ft_blue(array) -> array:
    '''
    Turn the color of the image to blue.
    '''
    new_array = array.copy()
    for i in range(len(new_array)):
        for j in range(len(new_array[i])):
            for k in range(len(new_array[i][j])):
                if k == 2:
                    pass
                elif k == 0 or k == 1:
                    new_array[i][j][k] = 0
    image = Image.fromarray(new_array)
    image.save("blue.jpg")
    return new_array


def ft_grey(array) -> array:
    '''
    Turn the color of the image to grey.
    '''
    new_array = array.copy()
    grey_array = np.zeros((len(array), len(array[0])), dtype=np.uint8)

    print(grey_array.shape)
    for i in range(len(new_array)):
        for j in range(len(new_array[i])):
            grey = int(new_array[i][j].mean())
            grey_array[i][j] = grey
    image = Image.fromarray(grey_array)
    image.save("grey.jpg")
    return grey_array
