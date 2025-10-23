# MATRIX OPERATION

this is a comprensive menu driven command line application for performung algebra operation using matrices

### GOAL

* used them using core  python

* using them without external libraries(numpy,panda etc.)

### KEYFEATURES

Key Features

 * **Core Python Only**: All logic is implemented using native Python data structures (lists of lists) and recursion.
* **Modular Design**: Code is separated into "main_app.py" and "matrix_lib.py"
* **Robust Validation:** Includes strict checks for dimension compatibility (e.g., for addition, multiplication) and mathematical constraints (e.g., square check for determinant, transppose,inverse).
* **User-Friendly Interface:** Interactive, menu-driven system for easy operation selection and matrix management.

### Installation and Setup

Since this project uses no external dependencies, simply clone the repository or save the two files (`mainapp.py` used for executin and interfaca and `matrix_lib.py` used for logic) into the **same directory**.

### How to Run the Application

1.  Open your terminal or command prompt (or use the VS Code Terminal).
2.  Navigate to the directory where you saved the files.
3.  Run the main application script:

    ```bash
    python mainapp.py
    ```

4.  The interactive menu will appear, prompting you for your choice. 

### operation

| Menu Option | Operation | Compatibility Check |
| :---: | :--- | :--- |
| **1** | create store matrix| creating a matrix for other operation
| **2** | Addition (`A + B`) | Must have identical dimensions. |
| **3** | Subtraction (`A - B`) | Must have identical dimensions. |
| **4** | Multiplication (`A * B`) | Columns of A must equal Rows of B. |
| **5** | Transpose (`Aᵀ`) | No dimensional constraints. |
| **6** | Determinant (`det(A)`) | Must be a square matrix. |
| **7** | Adjoint (`Adj(A)`)  | Must be a square matrix. |
| **8** | Inverse (`A⁻¹`) | Must be a square matrix AND non-singular ($\det(A) \neq 0$). |


### conclusion 

this will help to understand the concept of core matrix without using external libraries