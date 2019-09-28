#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
4. Median of Two Sorted Arrays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@author: houxue
@date: 2017/3/23
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        nums3 = []

        i, j, k = 0, 0, 0
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        if i < len1:
            nums3.extend(nums1[i:])

        if j < len2:
            nums3.extend(nums2[j:])

        total_len = len1 + len2
        if total_len % 2 == 0:
            return sum(nums3[total_len//2-1: total_len//2+1]) / 2
        else:
            return nums3[total_len//2]

    def find_median_sorted_arrays(self, nums1, nums2):
        """bin-search
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.find_kth_num(nums1, nums2, n//2+1)
        else:
            smaller = self.find_kth_num(nums1, nums2, n//2)
            greater = self.find_kth_num(nums1, nums2, n//2+1)
            return (smaller + greater) / 2.0

    def find_kth_num(self, nums1, nums2, k):
        """
        每次在A，B取前k/2个元素。有以下这些情况：
        1).  A的元素不够k/2. 则我们可以丢弃B前k/2. 反之亦然
        证明：
        我们使用反证法。
        假设第K大在B的前k/2中，例如位置在索引m(m <= k/2-1), 那么A必然拥有前k中的k-(m+1)个元素，
        而 m <= k/2-1,则 m+1 <= k/2, k-(m+1) > k/2与条件：A的元素不够k/2矛盾，所以假设不成立，得证。

        2). A[mid] < B[mid] (mid是k/2-1索引处的元素). 我们可以丢弃A前k/2。
        证明：
        我们使用反证法。
        假设第K大在A的前k/2中, 记为maxK，那么A[mid] >= maxK. 而B[mid] <= maxK, 推出A[mid]>=B[mid].
        与题设矛盾, 所以假设不能成立。
        :param nums1:
        :param nums2:
        :param k:
        :return:
        """
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])

        a = nums1[k//2-1] if len(nums1) >= k//2 else None
        b = nums2[k//2-1] if len(nums2) >= k//2 else None

        if b is None or (a is not None and a < b):
            # if nums2中的元素不足k/2, 或者nums1[k/2-1] < nums2[k/2-1],
            # 丢弃nums1的前k/2
            return self.find_kth_num(nums1[k//2:], nums2, k-k//2)
        else:
            # if nums1中的元素不足k/2, 丢弃nums2的前k/2
            return self.find_kth_num(nums1, nums2[k//2:], k-k//2)


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().find_median_sorted_arrays([1, 2], [3, 4]))
