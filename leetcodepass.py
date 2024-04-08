class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #遍历列表
        for i in range(len(nums)):
            #计算需要找到的另一个加数
            res = target - nums[i]
            #遍历剩下的列表，寻找是否存在计算出的另一个加数
            if res in nums[i+1:]:
                #如果有，即返回答案
                #首先nums[i+1:]是一个切片，它获取nums从i+1位置开始到最后的所有元素。然后.index(res)是为了得出符合要求的另一个加数在切片后的索引，也就是说原始列表中的i+1的索引对res来说是索引0
                #因此最后需要再加上i+1从而还原其在原始nums上的索引
                return [i,nums[i+1:].index(res) + i+1]

# 用户自行输入测试数组和目标和   
input_nums = input("请输入数组: ")
input_target = input("请输入目标和: ")

#需要将输入的字符串转换为整数列表，将输入的目标和转换为整数目标和
testnums = [int(num.strip())for num in input_nums.split(',')]
testtarget = int(input_target)

#创建test测试对象并调用twoSum方法
test = Solution()
result = test.twoSum(testnums,testtarget)
print(result)
