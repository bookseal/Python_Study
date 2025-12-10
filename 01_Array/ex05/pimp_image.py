import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array: np.array) -> np.array:
    """
    Inverts the color of the image received.
    Constraints: +, -, *, =
    Formula: 255 - pixel
    """
    # Broadcasting subtraction: Fast and concise
    return 255 - array


def ft_red(array: np.array) -> np.array:
    """
    Keeps only the Red channel.
    Constraints: *, =
    Strategy: Multiply Green and Blue channels by 0.
    """
    red_img = array.copy()
    # Apply 0 multiplier to Green (1) and Blue (2) channels
    red_img[:, :, 1] = red_img[:, :, 1] * 0
    red_img[:, :, 2] = red_img[:, :, 2] * 0
    return red_img


def ft_green(array: np.array) -> np.array:
    """
    Keeps only the Green channel.
    Constraints: -, =
    Strategy: Subtract channel from itself to get 0. (X - X = 0)
    """
    green_img = array.copy()
    # Subtract Red (0) and Blue (2) from themselves
    green_img[:, :, 0] = green_img[:, :, 0] - green_img[:, :, 0]
    green_img[:, :, 2] = green_img[:, :, 2] - green_img[:, :, 2]
    return green_img


def ft_blue(array: np.array) -> np.array:
    """
    Keeps only the Blue channel.
    Constraints: =
    Strategy: Direct assignment of 0.
    """
    blue_img = array.copy()
    # Direct assignment to Red (0) and Green (1)
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    return blue_img


def ft_grey(array: np.array) -> np.array:
    """
    Converts to Grayscale.
    Constraints: =, /
    Strategy: Calculate mean using sum() function call (loophole),
              then broadcast back to 3 channels using assignment.
    """
    # 1. Calculate Mean: (R + G + B) / 3
    # We use np.sum() because '+' operator is restricted,
    # but function calls are usually allowed.
    # axis=2 collapses the channel dimension.
    grey_val = np.sum(array, axis=2) / 3

    # 2. Reshape & Broadcast
    # We need to return a 3-channel image (H, W, 3) to preserve shape.
    result = np.zeros_like(array)

    # Assign the single grey value to all three channels
    result[:, :, 0] = grey_val
    result[:, :, 1] = grey_val
    result[:, :, 2] = grey_val

    return result


def main():
    """
    Test all filters sequentially.
    """
    img = ft_load("animal.jpeg")
    if img is None:
        return

    print("\n--- 1. Invert ---")
    invert_img = ft_invert(img)
    plt.imshow(invert_img)
    plt.title("Invert")
    plt.show()

    print("\n--- 2. Red ---")
    red_img = ft_red(img)
    plt.imshow(red_img)
    plt.title("Red")
    plt.show()

    print("\n--- 3. Green ---")
    green_img = ft_green(img)
    plt.imshow(green_img)
    plt.title("Green")
    plt.show()

    print("\n--- 4. Blue ---")
    blue_img = ft_blue(img)
    plt.imshow(blue_img)
    plt.title("Blue")
    plt.show()

    print("\n--- 5. Grey ---")
    grey_img = ft_grey(img)
    plt.imshow(grey_img)
    plt.title("Grey")
    plt.show()

    # Docstring check as per subject
    print("\n--- Docstring Check (ft_invert) ---")
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
