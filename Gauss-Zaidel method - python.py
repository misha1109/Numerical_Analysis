import numpy as np

def gause_zeidel_method(matrix, vector, tolerence, max_iterations):
    """Overall description:
       --------------------
       Gauss-Zaidel method - an iterative method to approximate the solution for: Ax = b
       where A is a matrix, b is a vector and x is the vector we aim to approximate.
       It is done so in gauss-zaidel method of approximation.
       
       Parameters:
       -----------
       matrix - matrix A.
       vector - vector b.
       tolerance - real number, the maximum error accepted.
       max_iterations - positive integer, the maximum number of iterations the method will perform.
       
       Output/Return:
       --------------
       x - the Nth iteration of the method, N depends on tolerence and max_iterations.
       The method will print the original equation system, each iteration
       and the final iteration - final approximation and error.
    """
    print("Original equation system:")
    for i in range(matrix.shape[0]):
        row = ["{0:3g}*x{1}".format(matrix[i, j], j + 1) for j in range(matrix.shape[1])]
        print("{0} = {1:3g}".format(" + ".join(row), vector[i]))
    print("--------------------")

    x = np.zeros_like(vector)
    for it_count in range(1, max_iterations):
        x_new = np.zeros_like(x)
        print("Iteration {0}, current approximation: {1}".format(it_count, x))
        for i in range(matrix.shape[0]):
            s1 = np.dot(matrix[i, :i], x_new[:i])
            s2 = np.dot(matrix[i, i + 1:], x[i + 1:])
            x_new[i] = (vector[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=tolerence):
            break
        x = x_new
    print("--------------------")

    print("Final approximation:")
    print(x)
    print("--------------------")
    error = np.dot(matrix, x) - vector
    print("Final error:")
    print(error)

A = np.array([[-1,-2,5],
              [4, -1, 1],
              [1, 6, 2]])

b = np.array([2,4,9])

gause_zeidel_method(A, b, 0.001, 20)