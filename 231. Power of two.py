class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n>0 and n%2==0):
            n=n/2
        return n==1
