import numpy as np

def jacobs_method(matrix, vector, tolerence, max_iterations):
    """Overall description:
       --------------------
       Jacobs method - an iterative method to approximate the solution for: Ax = b
       where A is a matrix, b is a vector and x is the vector we aim to approximate.
       It is done so in jacobs method of approximation.
       
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
        row = ["{}*x{}".format(matrix[i, j], j + 1) for j in range(matrix.shape[1])]
        print(" + ".join(row), "=", vector[i])
    print("-------------------------")
    
    iterations = 1
    x = np.zeros_like(vector)
    for it_count in range(max_iterations):
        print("Iteration {}".format(iterations) + ", Current approximation:", x)
        x_new = np.zeros_like(x)

        for i in range(matrix.shape[0]):
            s1 = np.dot(matrix[i, :i], x[:i])
            s2 = np.dot(matrix[i, i + 1:], x[i + 1:])
            x_new[i] = (vector[i] - s1 - s2) / matrix[i, i]

        if np.allclose(x, x_new, atol=tolerence, rtol=0.):
            break

        x = x_new
        iterations = iterations + 1
        
    print("-------------------------")
    print("Final approximation:")
    print(x)
    print("-------------------------")
    error = np.dot(matrix, x) - b
    print("Final error:")
    print(error)

A = np.array([[-1., -2., 5.],
              [4., -1., 1.],
              [1., 6., 2.]])

b = np.array([2., 4., 9])

jacobs_method(A, b, 0.001, 20)