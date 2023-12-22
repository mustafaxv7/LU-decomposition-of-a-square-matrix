import numpy as np
'''                      Nadour Moustafa    TP Work {Décomposition LU d'une matrice carrée}                                  '''
'''
Ce programme implémente la décomposition LU d'une matrice carrée et la résolution d'un système
d'équations linéaires.
'''
def decomposition_LU(A,threshold=1e-7):
    """
        Decomposes a square matrix A into its upper triangular matrix U and lower triangular matrix L.

        Args:
            A: A square NumPy array.

        Returns:
            L: The lower triangular matrix of the decomposition.
            U: The upper triangular matrix of the decomposition.
        """
    matrix = np.array(A,dtype='f')
    if len(matrix) != len(matrix[0]):
        return 'Please enter square function'
    if np.linalg.det(matrix) == 0:
        return 'Infinitely many or no solutions'
    else:
        n = len(matrix)
        L = np.eye(n)
        U = matrix.copy()
        for k in range(n):
            for i in range(k+1,n):
                L[i][k] = U[i][k] / U[k][k]
                for j in range(k,n):
                    U[i][j] = U[i][j] - (L[i][k] * U[k][j])
        U[np.abs(U) < threshold] = 0
    return L , U

def system_resolution(L,U,b):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)
    # Step (Ly = b)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] = y[i] - (L[i][j] * y[j])
    # Step (Ux = y)
    for i in range(n-1,-1,-1):
        x[i] = y[i]
        for j in range(i+1,n):
            x[i] = x[i] - (U[i][j] * x[j])
        x[i] = x[i] / U[i][i]
    return x

def fill_matrix(n):
    matrix = []
    for l in range(n):
        vector = []
        for c in range(n):
            element = float(input(f'\nEnter The Element number [{l+1}][{c+1}]: '))
            vector.append(element)
        matrix.append(vector)
    return matrix

def print_matrix(matrix,n):
    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j] : .2f}',end='  ')
        print()
def fill_vector(n):
    vector = []
    for i in range(n):
        element = float(input(f'\n\t\tEnter The Element number [{i+1}]: '))
        vector.append(element)
    return vector
print('\n\n\t\t\t\t\t\t\t\t\t\t*** Décomposition LU d\'une matrice carrée *** \n\n')
while True:
    try:
        n = int(input('Enter The number of lignes: '))
    except ValueError:
        print('Please Enter an Integer')
        continue
    if n >= 2 :
        break
    else:
        print('\nPlease Enter The number of lignes  greater then or equal 2\n')

print('\nFill The Matrix A: \n')
a = fill_matrix(n)
print('\nTreatement of matrix ...\n')
print()
print_matrix(a,n)
print()
det = np.linalg.det(a)
if det != 0:
    print('\nFill The Vector B: \n')
    b = fill_vector(n)
    print('\nAnalysing The System....\n\n')

    L,U = decomposition_LU(a)

    print('\n\t\t\t\t\t\t\t\t\t\t\t\t*** Analysis completed ***')
    print(f'\nL = \n')
    print_matrix(L,n)
    print(f'\nU = \n')
    print_matrix(U,n)
    x = system_resolution(L, U, b)
    print(f'\nx = {x}')
    j = 0
    for i in x:
        print(f'\nx{j} = {i: .2f}')
        j += 1
else:
    print('There is no limit of solutions det(a) = 0')

