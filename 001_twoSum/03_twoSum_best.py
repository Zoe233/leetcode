# -*- coding:utf-8 -*-
# 执行用时为36ms的范例
class Solution:
    def twoSum(self,nums,target):
        complement = {}

        for i in range(len(nums)):
            print(complement)
            if nums[i] in complement:
                return [complement[nums[i]],i]
            else:
                complement[target - nums[i]] = i


if __name__=='__main__':
    s = Solution()
    answer_list = s.twoSum([2,5,5,5,5,15], 10)
    print(answer_list) # [1,2]
    # 所以此处还有对题目的理解，之所以我的更复杂是因为可以返回多个，而不是一个获取到就直接return
    # 这个应该不严谨， 并不是真正的最佳答案吧。
