# import matplotlib
# matplotlib.use("TkAgg")  # enlever avant correction !!!!!!
import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the colors of the image.

    Args:
        array (ndarray): Original RGB image as a NumPy array.

    Returns:
        ndarray: Image with inverted colors.
    """

    plt.imshow(array)
    plt.title("Original")
    plt.axis('off')
    plt.show()
    inverted = array.copy()
    inverted = 255 - inverted
    plt.imshow(inverted)
    plt.title("Invert")
    plt.axis('off')
    plt.show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red channel, zeroes out green and blue.

    Args:
        array (ndarray): Original RGB image as a NumPy array.

    Returns:
        ndarray: Image with only red visible.
    """

    red_img = array.copy()
    red_img[:, :, 1] = 0
    red_img[:, :, 2] = 0
    plt.imshow(red_img)
    plt.title("Red")
    plt.axis('off')
    plt.show()
    return red_img


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel, zeroes out red and blue.

    Args:
        array (ndarray): Original RGB image as a NumPy array.

    Returns:
        ndarray: Image with only green visible.
    """

    green_img = array.copy()
    green_img[:, :, 0] = 0
    green_img[:, :, 2] = 0
    plt.imshow(green_img)
    plt.title("Green")
    plt.axis('off')
    plt.show()
    return green_img


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel, zeroes out red and green.

    Args:
        array (ndarray): Original RGB image as a NumPy array.

    Returns:
        ndarray: Image with only blue visible.
    """

    blue_img = array.copy()
    blue_img[:, :, 1] = 0
    blue_img[:, :, 0] = 0
    plt.imshow(blue_img)
    plt.title("Blue")
    plt.axis('off')
    plt.show()
    return blue_img


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale using the average of RGB values,
    then replicates this average across the 3 channels to keep the same shape.

    Args:
        array (ndarray): RGB image as a NumPy array of shape (H, W, 3).

    Returns:
        ndarray: Grayscale image as an array of shape (H, W, 3).
    """

    grey_img = array.copy()

    # Compute the mean across RGB channels → image in grayscale (H, W)
    grey_img = np.mean(array, axis=2)

    # Stack the same grayscale layer 3 times → (H, W, 3)
    grey_rgb = np.stack([grey_img, grey_img, grey_img], axis=2)

    # Display the grayscale image
    plt.imshow(grey_rgb.astype(np.uint8))  # cast to uint8 bc np.mean=float
    plt.title("Grey")
    plt.axis('off')
    plt.show()
    return grey_rgb

# axis=0 column
# axis=1 lines
# axis=2 RGB
