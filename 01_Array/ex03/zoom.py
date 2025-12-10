import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """
    Loads an image, slices it to a specific region, and displays it.
    The slicing operation reduces dimensions to (400, 400, 1).
    """
    # 1. Load Data (Module Reuse)
    # Using the robust loader from Ex02.
    # Expected shape: (768, 1024, 3) for 'animal.jpeg'
    img = ft_load("animal.jpeg")

    # Safety Check: If loading failed, stop immediately.
    if img is None:
        return

    # 2. Define ROI (Region of Interest)
    # We need a 400x400 square.
    # Coordinates are chosen to center on the raccoon's face.
    start_y, end_y = 100, 500  # Height: 400
    start_x, end_x = 450, 850  # Width:  400

    # 3. The Surgical Slicing (The Core Logic) [cite: 156]
    # Slicing syntax: [Y-axis, X-axis, Channel-axis]
    # 0:1 slice on the channel axis preserves the 3D structure (H, W, 1)
    # instead of flattening it to 2D (H, W).
    # This acts as a 'Red Channel Filter' conceptually.
    zoomed_img = img[start_y:end_y, start_x:end_x, 0:1]

    # 4. Status Report [cite: 156]
    print(f"New shape after slicing: {zoomed_img.shape}")
    print(zoomed_img)

    # 5. Visualization [cite: 140, 144]
    # 'cmap=gray' is required because we are plotting a single channel.
    # Without it, Matplotlib applies a default color map (viridis).
    plt.imshow(zoomed_img, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()

