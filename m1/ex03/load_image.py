import os
import numpy as np
from PIL import Image
from array import array


def ft_load(path: str) -> array:
    '''
    Load an image from the specified path and return a Numpy array.

    Parameters:
    path (str): Image

    Returns:
    array: NumPy array with pixels of the image
    '''
    try:
        if not path.lower().endswith(('jpg', 'jpeg')):
            raise AssertionError('formats allowed: JPG and JPEG')
        if not os.path.exists(path):
            raise AssertionError('File not found:', path)
        with Image.open(path) as img:
            img_array = np.array(img)
            print("The shape of image is:", img_array.shape)
            print(img_array)
            return img_array
    except AssertionError as e:
        print(e)
        return []
