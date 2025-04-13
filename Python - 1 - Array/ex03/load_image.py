from PIL import Image
from PIL import UnidentifiedImageError
import sys
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Loads a JPEG image and returns its RGB pixel data as a NumPy array.

    Prints the shape of the image as (height, width, 3). The function expects
    a valid JPEG file and handles errors related to path or format.

    Args:
        path (str): Path to the JPEG image file.

    Returns:
        ndarray: A NumPy array representing the image in RGB format.
    """

    try:
        img = Image.open(path)
        img = img.convert("RGB")
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
        sys.exit(1)
    except UnidentifiedImageError:
        print("Error: The file is not a valid JPEG image.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    data = np.array(img)
    print(f"The shape of image is: {data.shape}")
    return data
