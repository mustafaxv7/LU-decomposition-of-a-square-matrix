# LU-decomposition-of-a-square-matrix

      *** This program implements LU decomposition and resolves linear equations. ***

# Fonctions: 

      // decomposition_LU(A, threshold=1e-7): Decomposes a square matrix A into its triangular matrix
         lower L and its upper triangular matrix U.
         
     // system_resolution(L, U, b): Solves the system of linear equations LUx = b.
     
     // fill_matrix(n, m): Fills a matrix of size n x m with values entered by the user.
     
     // fill_vector(n): Fills a vector of size n with values entered by the user.
     
# PROGRAMME IMPLEMENTATION:

     1. The user enters the size of the matrix A (n rows and m columns).
     
     2. The program checks whether the matrix is square and its determinant is non-zero.
     
     3. If the matrix is valid, the program breaks it down into L and U using the decomposition_LU function.
     
     4. The program then resolves the system of equations LUx = b using the system_resolution function.
     
     5. The program displays the matrices L and U, as well as the solution of the system of equations x.
