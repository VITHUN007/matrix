import sys
from matrix_lib import (
    print_matrix,
    matrix_add, matrix_subtract, matrix_multiply,
    matrix_transpose, matrix_determinant,
    matrix_adjoint, matrix_inverse
)

def create_matrix_from_input():
    while True:
        try:
            rows = int(input("Enter the number of rows (m): "))
            cols = int(input("Enter the number of columns (n): "))
            if rows <= 0 or cols <= 0:
                print("Dimensions must be positive integers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter integers for dimensions.")
            
    matrix = []
    print(f"\nEnter the elements for the {rows}x{cols} matrix:")
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Row {i+1} (space-separated {cols} elements): ").split()

                if len(row_input) != cols:
                    print(f"Must enter exactly {cols} elements.")
                    continue
                
                row = [float(x) for x in row_input]
                break
            except ValueError:
                print("Invalid input. All elements must be numbers.")
        matrix.append(row)
    return matrix

def get_stored_matrix(store, name_prompt):
    name = input(name_prompt).upper()
    
    if name not in store:
        raise KeyError(f"Matrix '{name}' not found.")
    return store[name], name

def matrix_menu():
    matrix_store = {}
    while True:
        print("\n" + "="*50)
        print("MATRIX OPERATIONS MENU")
        print("="*50)

        if matrix_store:
            print("Stored Matrices:")
            for name, matrix in matrix_store.items():
                r = len(matrix); c = len(matrix[0])
                print(f"  - {name}: {r}x{c}")

        else:
            print("No matrices currently stored.")
        print("-" * 50)  
        print("1. Create/Store a new Matrix")
        print("2. Addition (A + B)")
        print("3. Subtraction (A - B)")
        print("4. Multiplication (A * B)")
        print("5. Transpose (A^T)")
        print("6. Determinant (det(A))")
        print("7. Adjoint (Adj(A))")
        print("8. Inverse (A⁻¹)")
        print("9. Print Stored Matrix")
        print("0. Exit")
        print("-" * 50)

        choice = input("Enter your choice (0-9): ")  
        try:
            if choice == '0':
                print("Exiting Matrix Operations Module. Goodbye!")
                sys.exit()

            elif choice == '1':
                new_matrix = create_matrix_from_input()
                name = input("Enter a name to store this matrix (e.g., A, B): ").upper()
                matrix_store[name] = new_matrix
                print(f"Matrix '{name}' created and stored.")
                print_matrix(new_matrix)

            elif choice in ('2', '3', '4'):
                if len(matrix_store) < 2:
                    print("Need at least two stored matrices (A and B).")
                    continue
                    
                A, name_A = get_stored_matrix(matrix_store, "Enter name for A: ")
                B, name_B = get_stored_matrix(matrix_store, "Enter name for B: ")

                Result = None
                if choice == '2':
                    Result = matrix_add(A, B); op_symbol, op_name = '+', "Addition"

                elif choice == '3':
                    Result = matrix_subtract(A, B); op_symbol, op_name = '-', "Subtraction"

                elif choice == '4':
                    Result = matrix_multiply(A, B); op_symbol, op_name = '*', "Multiplication"
                    
                print(f"\n Result of {op_name} ({name_A} {op_symbol} {name_B}):")
                print_matrix(Result)
                    
            elif choice in ('5', '6', '7', '8'):
                if not matrix_store:
                    print("Need at least one stored matrix.")
                    continue
                    
                A, name_A = get_stored_matrix(matrix_store, "Enter the matrix name: ")
                
                Result = None
                if choice == '5':
                    Result = matrix_transpose(A); op_name = "Transpose"

                elif choice == '6':
                    det = matrix_determinant(A)
                    print(f"\n Result of Determinant (det({name_A})): {det:g}")

                elif choice == '7':
                    Result = matrix_adjoint(A); op_name = "Adjoint"

                elif choice == '8':
                    Result = matrix_inverse(A); op_name = "Inverse"
                
                if choice != '6' and Result is not None:
                    print(f"\n Result of {op_name} of {name_A}:")
                    print_matrix(Result)
                
            elif choice == '9':
                if not matrix_store:
                    print("No matrices stored.")
                    continue
                A, name = get_stored_matrix(matrix_store, "Enter the name of the matrix to print: ")
                print(f"\nMatrix '{name}':")
                print_matrix(A)
                
            else:
                print("Invalid choice. Please select an option from 0 to 9.")

        except (ValueError, KeyError) as e:
            print(f"\n **Operation Failed:** {e}")
        except Exception as e:
            
            print(f"\n **An unexpected error occurred:** {e}")

if __name__ == "__main__":
    matrix_menu()

