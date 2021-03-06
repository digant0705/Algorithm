# -*- coding: utf-8 -*-

'''
Factorial Trailing Zeroes
=========================

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''


class Solution(object):
    '''算法思路：

    观察规律可以看到，尾 0 的个数与 <= n 的数中 5 的个数相等
    '''
    def trailingZeroes(self, n):
        count, div = 0, n
        while div:
            div /= 5
            count += div
        return count


s = Solution()
print s.trailingZeroes(100)
