import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncate a 2D array using slicing and print its shapes.

    Args:
        family: A 2D list of numbers.
        start: Starting index for slicing.
        end: Ending index for slicing.

    Returns:
        The truncated 2D list.
        Returns an empty list [] if an error occurs.
    """
    # 1. Validation & Memory Loading
    # Reject immediately if input is not a list
    if not isinstance(family, list):
        print("Error: Input must be a list.")
        return []

    try:
        # Attempt to convert to Numpy Array.
        # If inner list lengths vary (Jagged List), Numpy creates an
        # object array or raises an error here.
        family_arr = np.array(family)

        # 2. Structural Integrity Check
        # If not a 2D matrix, this function serves no purpose.
        if family_arr.ndim != 2:
            print("Error: Input must be a 2D list with consistent "
                  "row lengths.")
            return []

        # 3. Initial Status Report
        print(f"My shape is: {family_arr.shape}")

        # 4. The Surgical Slicing (View Operation)
        # Slice rows based on the start:end range.
        # Numpy slicing creates a 'View' without copying data,
        # ensuring memory efficiency.
        truncated_arr = family_arr[start:end]

        # 5. Post-Op Status Report
        print(f"My new shape is: {truncated_arr.shape}")

        # 6. Return as List
        # At this point, it converts to a Python List, triggering
        # actual data copying.
        return truncated_arr.tolist()

    except Exception as e:
        # Gracefully handle any runtime errors
        print(f"Error: {e}")
        return []


def main():
    """
    Test cases as per the subject requirements.
    """
    # Test Data from PDF
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print("--- Test 1: Standard Case (0 to 2) ---")
    print(slice_me(family, 0, 2))

    print("\n--- Test 2: Standard Case (1 to -2) ---")
    print(slice_me(family, 1, -2))

    print("\n--- Test 3: Error Case (Jagged List) ---")
    # Mixed list lengths -> Error during Numpy conversion or ndim != 2
    jagged_family = [[1.80, 78.4], [2.15]]
    print(slice_me(jagged_family, 0, 2))

    print("\n--- Test 4: Error Case (Not a List) ---")
    print(slice_me("Not a list", 0, 2))


if __name__ == "__main__":
    main()
