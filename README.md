# Python Data Science - Array: The Architect's Perspective

> **From C-Style Memory Management to High-Performance Vectorization**
> *42 Seoul Python Piscine - Array Module*

## 📋 Overview
This repository documents my transition from low-level C programming (Ecole 42) to **Data Engineering & MLOps**.
Instead of treating Python as a simple scripting language, I approached this project with a **Solution Architect's mindset**: focusing on **memory efficiency, hardware acceleration (SIMD), and data pipeline integrity**.

The goal was not just to solve algorithmic problems, but to understand the **computational cost** of data manipulation in large-scale AI systems.

---

## 🏗 Architectural Insights & Key Takeaways

As an aspiring **AI Solutions Architect**, I interpreted these exercises as a simulation of real-world data processing challenges:

### 1. Hardware Acceleration over Loops (The "No-Loop" Policy)
* **Insight:** Traditional Python `for-loops` introduce massive overhead due to dynamic type checking.
* **Solution:** Leveraged **Numpy Broadcasting (SIMD)**.
* **Impact:** In a real-world MLOps pipeline, this shift reduces data processing latency from seconds to milliseconds, enabling real-time inference.

### 2. Zero-Copy Data Slicing (Memory Views)
* **Insight:** Copying large datasets (e.g., 4K images, massive log streams) spikes RAM usage and cost.
* **Solution:** Utilized **Slicing as a View**, not a Copy.
* **Impact:** Manipulating data pointers instead of duplicating memory blocks is crucial for optimizing cloud resource costs (AWS/GCP) when handling Terabytes of data.

### 3. Data Normalization (Input Gatekeeping)
* **Insight:** Inconsistent input formats (RGBA vs RGB, Jagged Lists) cause downstream model failures.
* **Solution:** Implemented strict **Data Validation & Normalization** layers at the ingestion point (e.g., forcing RGB conversion).
* **Impact:** Prevents "Garbage In, Garbage Out," ensuring the stability of AI Training/Inference pipelines.

---

## 🛠 Module Breakdown

### Ex00: Give my BMI (Vectorization)
* **Challenge:** Process mass health data without loops.
* **Architectural Approach:** Implemented **Vectorized Operations** to handle calculations in batches. Used `try-except` blocks for robust error handling against invalid inputs (e.g., size mismatch).

### Ex01: 2D Array (Slicing)
* **Challenge:** Extract specific data regions from a server-rack-like 2D dataset.
* **Architectural Approach:** Utilized **Numpy Slicing** to create efficient views of the dataset. Implemented structural integrity checks (`.ndim`, `.shape`) to reject jagged arrays before processing.

### Ex02: Load my Image (Normalization)
* **Challenge:** Ingest various image formats for processing.
* **Architectural Approach:** Enforced a **Standardization Protocol** converting all inputs (PNG, Grayscale) to strictly `(H, W, 3)` RGB format. This ensures predictable tensor shapes for downstream tasks.

### Ex03: Zoom on Me (Dimensionality Reduction)
* **Challenge:** Crop and process specific regions of an image.
* **Architectural Approach:** Performed **Channel Slicing** (`0:1`) to reduce dimensions while preserving the 3D tensor structure `(H, W, 1)`, simulating data projection techniques.

### Ex04: Rotate Me (The "Raw Metal" Transpose)
* **Challenge:** Rotate an image without using `np.transpose()` or `.T`.
* **Architectural Approach:** Manually implemented the **Index Swapping Algorithm** (`[j][i] = [i][j]`) using nested loops. This exercise highlighted the importance of optimized libraries by demonstrating the computational cost of manual memory access patterns.

### Ex05: Pimp My Image (Kernel Logic)
* **Challenge:** Implement image filters (Invert, Red, Grey) using restricted arithmetic operators.
* **Architectural Approach:**
    * **Invert:** Used Broadcasting subtraction (`255 - Array`).
    * **Grayscale:** Exploited function call permissions to use `np.sum()` combined with broadcasting assignment, proving that creative engineering can bypass syntactic constraints while maintaining data integrity.

---

## 💻 Tech Stack
* **Language:** Python 3.10
* **Core Library:** Numpy (for SIMD & Memory Management)
* **Visualization:** Matplotlib (for Data Inspection)
* **Image Processing:** Pillow (PIL)

## 🚀 How to Run
```bash
# Clone the repository
git clone [https://github.com/your-username/python-data-science-array.git](https://github.com/your-username/python-data-science-array.git)

# Install dependencies
pip install numpy matplotlib flake8 pillow

# Run specific modules (e.g., Ex00)
python3 ex00/give_bmi.py