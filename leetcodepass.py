class Solution(object):
    #两数之和
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

# # 用户自行输入测试数组和目标和   
# input_nums = input("请输入数组: ")
# input_target = input("请输入目标和: ")

# #需要将输入的字符串转换为整数列表，将输入的目标和转换为整数目标和
# testnums = [int(num.strip())for num in input_nums.split(',')]
# testtarget = int(input_target)

# #创建test测试对象并调用twoSum方法
# test = Solution()
# result = test.twoSum(testnums,testtarget)
# print(result)

    #移动零解法1：引入新数组
    def moveZeroes1(self,nums):
        result = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
            else:
                zero_count += 1
        result.extend([0]*zero_count)
        return result

# test = Solution()
# # nums = input("请输入数组：")
# # test_nums = [int(num.strip("[]")) for num in nums.split(',') ]
# # print(test_nums)
# results = test.moveZeroes([0, 1, 0, 3, 12])
# print(results)
    
    # 移动零解法2——双指针：两次遍历
    def moveZeroes2(self,nums):
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(j,len(nums)):
            nums[i] = 0

        return nums

# test = Solution()
# nums = input("请输入数组：")
# test_nums = eval(nums)
# print(test_nums)
# results = test.moveZeroes2(test_nums)
# print(results)


    #移动零解法3——双指针：一次遍历
    def moveZeroes3(self,nums):
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
        return nums
    
# test = Solution()
# nums = input("请输入数组：")
# test_nums = eval(nums)
# result = test.moveZeroes3(test_nums)
# print(result)

    #相交链表
    def getIntersectionNode(self,headA,headB):
        s = set()
        p,q = headA,headB

        while p:
            s.add(p)
            p = p.next

        while q:
            if q in s:
                return q
            q = q.next
        return None

    # 反转链表解法1:双指针
    def reverseList(self, head):
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    
    # 反转链表解法2:递归
    def reverseList(self,head):
        def reverse(cur,pre):
            if cur == None:
                return pre
            tmp = cur.next
            cur.next = pre

            return reverse(tmp, cur)
        
        return reverse(head, None)
            
