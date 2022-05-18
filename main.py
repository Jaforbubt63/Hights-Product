class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        n = len(A)
        A.sort()
        prod1 = A[-1] * A[-2] * [-3]
        prod2 = A[0] * A[1] * A[-1]
        return max(prod1, prod2)
