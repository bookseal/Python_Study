import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """
    Loads an image, cuts a square part, and performs a manual transpose.
    Constraints: No numpy.transpose() or .T allowed.
    """
    # 1. Load Data
    img = ft_load("animal.jpeg")
    if img is None:
        return

    # 2. Cut a Square Part (Pre-requisite for Transpose)
    # Reuse the ROI from Ex03 to ensure a 400x400 square.
    # Slicing: [Y, X, C] -> 0:1 preserves the channel dimension (H, W, 1)
    cut_img = img[100:500, 450:850, 0:1]

    # Validation: Transpose requires a square matrix for simple swapping
    height, width, channel = cut_img.shape
    if height != width:
        print("Error: Transpose logic requires a square image.")
        return

    # 3. Memory Allocation (The Architect's Optimization)
    # Create an empty container first to avoid dynamic reallocation overhead.
    # The shape becomes (Width, Height, Channel).
    transposed_data = np.zeros((width, height, channel), dtype=cut_img.dtype)

    # 4. Manual Transpose (The Core Constraint)
    # "You have to do the transpose yourself"
    # Nested loops to swap row (i) and column (j) indices.
    for i in range(height):
        for j in range(width):
            # The Swap Logic: Target[j][i] <== Source[i][j]
            transposed_data[j][i] = cut_img[i][j]

    # 5. Status Report [cite: 188]
    # Expected output includes shape and data printing.
    print(f"New shape after Transpose: {transposed_data.shape}")
    print(transposed_data)

    # 6. Visualization
    # Display the transposed (and seemingly rotated+mirrored) image.
    plt.imshow(transposed_data, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
