import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Loads an image from a file, converts it to RGB format,
    prints its shape and pixel content, and returns it as a Numpy array.

    Args:
        path: The path to the image file.

    Returns:
        A Numpy array representing the image in RGB format.
        Returns None if an error occurs.
    """
    try:
        # 1. Resource Management
        # Using 'with' ensures the file is closed automatically.
        with Image.open(path) as img:

            # 2. Data Normalization (The Architect's Key Step)
            # Force convert to RGB (3 channels) to guarantee output shape.
            # This handles RGBA or Grayscale inputs safely.
            img = img.convert('RGB')

            # 3. Memory Loading
            # Convert the image object into a raw Numpy array.
            data = np.array(img)

            # 4. Status Report
            # Print dimensions: (Height, Width, Channel)
            print(f"The shape of image is: {data.shape}")

            # Print raw pixel data as requested by the subject
            print(data)

            return data

    except Exception as e:
        # 5. Error Handling
        print(f"Error: {e}")
        return None


def main():
    """
    Test cases to verify the function behavior.
    """
    print("--- Test 1: Loading a valid image ---")
    # Make sure you have 'animal.jpeg' or similar file
    ft_load("animal.jpeg")

    print("\n--- Test 2: Error Handling (File not found) ---")
    ft_load("ghost_file.jpg")

    print("\n--- Test 3: Error Handling (Not an image) ---")
    with open("test.txt", "w") as f:
        f.write("This is not an image.")
    ft_load("test.txt")


if __name__ == "__main__":
    main()
