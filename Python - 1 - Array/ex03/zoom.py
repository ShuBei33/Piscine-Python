# import matplotlib
# matplotlib.use("TkAgg")  # enlever avant correction !!!!!!
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def zoom(data) -> np.array:
    """
    Displays the input image, extracts a 400x400 zoomed section
    centered (with offset) on the image, and shows the zoomed grayscale image.

    Args:
        data (ndarray): RGB image data loaded from ft_load().

    Returns:
        ndarray: The zoomed grayscale section as a 2D array.
    """

    plt.imshow(data)
    plt.axis('on')
    plt.show()
    height, width, _ = data.shape
    center_y = (height - 100) // 2
    center_x = (width + 200) // 2
    half = 200

    zoomed = data[
        center_y - half: center_y + half,
        center_x - half: center_x + half,
        0
    ]

    print(f"New shape after slicing: {zoomed.shape}")
    print(zoomed)
    plt.imshow(zoomed, cmap="gray")
    plt.axis('on')
    plt.show()
    return zoomed


def main():
    """
    Main function to load and process the image.
    """
    data = ft_load("animal.jpeg")
    print(data)
    print(zoom(data))


if __name__ == "__main__":
    main()

# For WSL at home only:
# import matplotlib
# matplotlib.use("TkAgg")
