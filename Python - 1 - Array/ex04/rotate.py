# import matplotlib
# matplotlib.use("TkAgg")  # enlever avant correction !!!!!!
from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def zoom(data) -> np.array:
    """
    Extracts a 400x400 zoomed section from the red channel of the image.

    Args:
        data (ndarray): RGB image as a NumPy array.

    Returns:
        ndarray: 2D array representing the zoomed red channel.
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

    # plt.imshow(zoomed, cmap="gray")
    # plt.axis('on')
    # plt.show()
    return zoomed


def transpose(data: np.array) -> np.array:
    """
    Manually transposes a 2D array (no use of np.transpose or .T).
    Prints the shape and contents of the transposed array.

    Args:
        data (ndarray): 2D NumPy array to transpose.

    Returns:
        ndarray: Transposed 2D NumPy array.
    """

    data_list = data.tolist()
    transp = []
    for x in range(len(data_list[0])):  # columns
        new_row = []
        for y in range(len(data_list)):  # lines
            new_row.append(data_list[y][x])
        transp.append(new_row)

    transp_array = np.array(transp)

    # Match expected output: (400, 400, 1)
    transp_array = np.expand_dims(transp_array, axis=2)  # 2 = add after dims

    print(f"The shape of image is: {transp_array.shape}")
    print(transp_array)
    return transp_array


def rotate(data: np.array) -> np.array:
    """
    Rotates a 2D array 90 degrees clockwise by reversing each row.
    Prints the new shape and contents, and displays the image.

    Args:
        data (ndarray): Transposed 2D NumPy array.

    Returns:
        ndarray: Rotated 2D NumPy array.
    """

    # transform 3d in 2d by removing last channel
    rot = data[:, :, 0].tolist()

    rot_array = rot[::1]  # copy all but in reverse
    rot_array = np.array(rot)

    print(f"New shape after Transpose: {rot_array.shape}")
    print(rot_array)

    plt.imshow(rot_array, cmap="gray")
    plt.axis('on')
    plt.show()
    return rot_array


def main():
    """
    Loads the image, zooms, transposes and rotates it,
    then prints and displays the final result.
    """

    data = ft_load("animal.jpeg")
    zoomed = zoom(data)
    transp = transpose(zoomed)
    rotate(transp)


if __name__ == "__main__":
    main()

# For WSL at home only:
# import matplotlib
# matplotlib.use("TkAgg")
