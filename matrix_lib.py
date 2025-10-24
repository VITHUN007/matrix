def get_dimensions(matrix):
    if not matrix:
        return 1,0
    return len(matrix), len(matrix[0])

def print_matrix(matrix):
    if not matrix:
        print("[]")
        return
    
    col_widths = [0] * len(matrix[0])
    for row in matrix:
        for j, elem in enumerate(row):
            col_widths[j] = max(col_widths[j], len(f"{elem:g}"))

    width = sum(col_widths) + 3 * len(col_widths) + 1
    print("-" * width)
    for row in matrix:
        print("| ", end="")
        for j, elem in enumerate(row):
            print(f"{elem:>{col_widths[j]}.3g}", end=" | ")
        print()
    print("-" * width)

    
def matrix_add(A, B):
    rows_A, cols_A = get_dimensions(A)
    rows_B, cols_B = get_dimensions(B)
    
    if rows_A != rows_B or cols_A != cols_B:
        raise ValueError("Matrices must have the same dimensions for addition.")
        
    return [[A[i][j] + B[i][j] for j in range(cols_A)] for i in range(rows_A)]

def matrix_subtract(A, B):
    rows_A, cols_A = get_dimensions(A)
    rows_B, cols_B = get_dimensions(B)
    
    if rows_A != rows_B or cols_A != cols_B:
        raise ValueError("Matrices must have the same dimensions for subtraction.")
        
    return [[A[i][j] - B[i][j] for j in range(cols_A)] for i in range(rows_A)]

def matrix_multiply(A, B):
    rows_A, cols_A = get_dimensions(A)
    rows_B, cols_B = get_dimensions(B)
    
    if cols_A != rows_B:
        raise ValueError("Cols of first matrix must equal rows of second matrix for multiplication.")
        
    C = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))
    return C

def matrix_transpose(A):
    rows, cols = get_dimensions(A)
    return [[A[i][j] for i in range(rows)] for j in range(cols)]

def get_minor(matrix, i, j):
    minor = []
    for row_index, row in enumerate(matrix):
        if row_index != i:
            new_row = [element for col_index, element in enumerate(row) if col_index != j]
            minor.append(new_row)
    return minor

def matrix_determinant(A):
    rows, cols = get_dimensions(A)
    if rows != cols:
        raise ValueError("Determinant can only be calculated for square matrices.")
        
    n = rows

    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
        
    det = 0
    for j in range(n):
        sign = (-1)**(j)
        minor_matrix = get_minor(A, 0, j)
        det += sign * A[0][j] * matrix_determinant(minor_matrix)
        
    return det

def matrix_adjoint(A):
    rows, cols = get_dimensions(A)
    if rows != cols:
        raise ValueError("Adjoint can only be calculated for square matrices.")
        
    n = rows
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            minor_det = matrix_determinant(get_minor(A, i, j))
            C[i][j] = ((-1)**(i + j)) * minor_det

    return matrix_transpose(C)
    
def matrix_inverse(A):
    rows, cols = get_dimensions(A)
    if rows != cols:
        raise ValueError("Inverse can only be calculated for square matrices.")
        
    det_A = matrix_determinant(A)
    
    if abs(det_A) < 1e-12: 
        raise ValueError("Determinant is zero. The matrix is singular and has no inverse.")
        
    Adj_A = matrix_adjoint(A)
    scalar = 1.0 / det_A
    n = rows
    
    return [[Adj_A[i][j] * scalar for j in range(n)] for i in range(n)]
