import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI from height and weight lists using Numpy broadcasting.
    Formula: weight / (height ^ 2)
    Input:
        height: List of heights in meters (int or float)
        weight: List of weights in kg (int or float)
    Output:
        List of BMI values (int or float)
    Error Handling:
        Prints error message and returns None if input sizes mismatch
        or types are incorrect.
    """
    # 1. Validation: Size Mismatch Check (O(1))
    if len(height) != len(weight):
        print("Error: Input lists must have the same size.")
        return None

    try:
        # 2. Memory Loading: Convert to Numpy Array for SIMD operations
        h_arr = np.array(height)
        w_arr = np.array(weight)

        # 3. Type Validation: Ensure inputs are numeric numbers
        # np.issubdtype checks if the array's data type is a subclass of np.number
        if not (np.issubdtype(h_arr.dtype, np.number) and
                np.issubdtype(w_arr.dtype, np.number)):
            print("Error: Lists must contain only integers or floats.")
            return None

        # 4. Calculation: Broadcasting (Vectorized Operation)
        # Avoids slow Python loops. Calculates all BMIs in one go.
        bmi_result = w_arr / (h_arr ** 2)

        # 5. Output: Convert back to Python list
        return bmi_result.tolist()

    except Exception as e:
        # Catch-all for unexpected runtime errors (e.g., division by zero)
        print(f"Error: {e}")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Filter BMI values based on a limit.
    Input:
        bmi: List of BMI values
        limit: Threshold integer
    Output:
        List of booleans (True if bmi > limit, else False)
    """
    try:
        # 1. Memory Loading
        bmi_arr = np.array(bmi)

        # 2. Type Validation
        if not np.issubdtype(bmi_arr.dtype, np.number):
            print("Error: BMI list must contain numbers.")
            return None

        # 3. Filtering: Boolean Broadcasting
        # Creates a boolean mask directly without if-else loops
        result = bmi_arr > limit

        # 4. Output
        return result.tolist()

    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """
    Main entry point for testing.
    This block is executed only when the script is run directly.
    """
    print("--- Test 1: Standard Case (from PDF) ---")
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    
    bmi = give_bmi(height, weight)
    print(f"BMI: {bmi}")
    print(f"Type: {type(bmi)}")
    
    if bmi is not None:
        print(f"Limit check (26): {apply_limit(bmi, 26)}")

    print("\n--- Test 2: Error Handling (Size Mismatch) ---")
    give_bmi([1.80], [70, 80])  # Should print Error

    print("\n--- Test 3: Error Handling (Wrong Types) ---")
    give_bmi(["tall"], ["heavy"])  # Should print Error


if __name__ == "__main__":
    main()