"""
Matrix chain multiplication is an optimization problem concerning the most efficient way to multiply a
given sequence of matrices. The problem is not actually to perform the multiplications, but merely to decide the
sequence of the matrix multiplications involved.

There are many options because matrix multiplication is associative. In other words, no matter how the product is
 parenthesized, the result obtained will remain the same. For example, for four matrices A, B, C, and D, there are
 five possible options:

((AB)C)D = (A(BC))D = (AB)(CD) = A((BC)D) = A(B(CD)).

Although it does not affect the product, the order in which the terms are parenthesized affects the number
of simple arithmetic operations needed to compute the product, that is, the computational complexity. F
or example, if A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix, then

computing (AB)C needs (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations, while
computing A(BC) needs (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
Clearly the first method is more efficient.

Checking each possible parenthesization (brute force) would require a run-time that is exponential in the number of
matrices, which is very slow and impractical for large n. A quicker solution to this problem can be achieved by
breaking up the problem into a set of related sub-problems.
"""


def optimal_matrix_chain_recursive(matrix_dims):
    """
    Return the product of the optimal computations.

    matrix_dims contains the dimensions of the matrix. e.g.
    [40, 20, 30] implies two matrices of shape [40, 20] and [20, 30].
    """
    assert len(matrix_dims) >= 2
    if len(matrix_dims) == 2:
        # Only one matrix
        return 0

    if len(matrix_dims) == 3:
        # Only one answer
        return matrix_dims[0] * matrix_dims[1] * matrix_dims[2]
    else:
        # Recursive: min_cost(ABC) = min(min_cost((AB)C), min_cost(A(BC))
        # (AB)C
        candidate1 = optimal_matrix_chain_recursive(matrix_dims[:-1])
        first_dim = matrix_dims[0]
        candidate1 += first_dim * matrix_dims[-2] * matrix_dims[-1]
        # A(BC)
        candidate2 = optimal_matrix_chain_recursive(matrix_dims[1:])
        candidate2 += first_dim * matrix_dims[1] * matrix_dims[-1]
        return min(candidate1, candidate2)


def optimal_matrix_chain_dp(dims):
    """
    Dynamic Programming version
    """
    n = len(dims)
    # min_costs[i, j] = minimum number of scalar multiplications (i.e., cost)
    # needed to compute matrix `M[i] M[i+1] … M[j] = M[i…j]`
    # The cost is zero when multiplying one matrix
    min_costs = [[0] * n for _ in range(n+1)]

    # Loop over all chains of length l = 0, 1, 2, ... n-1
    for l in range(2, n):
        # A chain of length l can start at 0, 1, ... n - chain_length position
        for i in range(1, n - l + 1):
            # end index of the chain in dims: add length of the chain to the start index
            j = i + l - 1
            # Calculate the min cost of multiplying M[i] M[i+1]..M[k] and M[k+1]...M[j]
            costs = []
            for k in range(i, j):
                cost = min_costs[i][k] + min_costs[k+1][j] + dims[i - 1] * dims[k] * dims[j]
                costs.append(cost)
            # Record this as min_costs[i][j]
            min_costs[i][j] = min(costs)

    return min_costs[1][n-1]


if __name__ == '__main__':
    matrix_dims = [10, 30, 5, 60]
    result = optimal_matrix_chain_dp(matrix_dims)
    print(result)
    assert result == 4500

    matrix_dims = [40, 20, 30, 10, 30]
    result = optimal_matrix_chain_dp(matrix_dims)
    print(result)
    assert result == 26000
    #
    matrix_dims = [10, 20, 30, 40, 30]
    result = optimal_matrix_chain_dp(matrix_dims)
    assert result == 30000


