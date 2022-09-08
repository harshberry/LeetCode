import numpy as np

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = [int(x) for x in str(n)]
        return np.prod(a) - np.sum(a)