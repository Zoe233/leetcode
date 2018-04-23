# -*- coding:utf-8 -*-
class Solution:
    '''
    来源：http://www.cnblogs.com/grandyang/p/4130379.html
    思路：
        1.遍历一遍数组，建立map数据
        2.再遍历一遍开始查找，找到则记录index
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Two-pass Hash Table
        Time complexity: O(n)
        Space complexity:O(n)
        """
        unordered_map = {}
        res = []
        for i in range(len(nums)):  # O(1)
            unordered_map[nums[i]] = i
        for i in range(len(nums)):  # O(n)
            t = target - nums[i]
            if unordered_map.get(t) != i and unordered_map.get(t):
                res.append(i)
                res.append(unordered_map.get(t))
                break
        return res

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        One-pass Hash Table 优化，将两个for循环合并成一个
        Time complexity: O(n)
        Space complexity:O(n)
        """
        unordered_map = {}
        res = []
        for i in range(len(nums)):
            t = target-nums[i]
            # print(t)
            if unordered_map.get(t) is not None:
                res.append(i)
                res.append(unordered_map.get(t))
                break
            unordered_map[nums[i]] = i
            # print(unordered_map)
        return res


if __name__=='__main__':
    s = Solution()
    answer_list = s.twoSum2([2,7,11, 15], 9)
    print(answer_list)