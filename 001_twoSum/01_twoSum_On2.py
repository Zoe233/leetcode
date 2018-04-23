class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        暴力破解的算法时间复杂度Time complexity为O(n^2) ==> Time Limit Exceeded
        Space complexity:O(n)
        第一遍，非优化版
        """
        answer_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    mid_sum = nums[i] + nums[j]
                    # print(mid_sum,i,j,nums[i],nums[j])
                    if mid_sum == target and i not in answer_list:
                        answer_list.append(i)
                        answer_list.append(j)
                mid_sum = 0
        return answer_list

    def twoSum2(self, nums ,target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Time complexity: O(n^2)
        Space complexity:O(n)
        优化了细节的处理，少了mid_sum的变量
        '''
        answer_list = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j] == target - nums[i] and i !=j and i not in answer_list:
                    answer_list.append(i)
                    answer_list.append(j)
        return answer_list

if __name__=='__main__':
    s = Solution()
    answer_list = s.twoSum([2,5,5,11],10)
    print(answer_list)
    answer_list2 = s.twoSum2([2,5,5,11],10)
    print(answer_list2)