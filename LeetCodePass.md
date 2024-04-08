# LeetCodePass

## 1. 两数之和

### 1.1 题目描述

> 给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出**和为目标值** *`target`* 的那**两个**整数，并返回它们的数组下标。
>
> 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
>
> 你可以按任意顺序返回答案。
>
> **示例 1：**
>
> ```
> 输入：nums = [2,7,11,15], target = 9
> 输出：[0,1]
> 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
> ```
>
> **示例 2：**
>
> ```
> 输入：nums = [3,2,4], target = 6
> 输出：[1,2]
> ```
>
> **示例 3：**
>
> ```
> 输入：nums = [3,3], target = 6
> 输出：[0,1]
> ```



### 1.2 题目解答

本题的详细思路参考LeetCode题解[直观的 Python 题解：思路推导&代码注释](https://leetcode.cn/problems/two-sum/solutions/1463966/jian-dan-python-by-chanemo-muld/?envType=study-plan-v2&envId=top-100-liked)

> **核心观念：编程实际上是用计算机实现人工能干的事情。**
> 因此解题可以遵循 “**人工推导——从个体到群体——从特殊到普遍**” 的思路，即从个例推出通解。

为了让自己带入思考，故选择示例2进行人工推导的思路展开：

如果让人来完成这道题，最简单的方式就是逐一排查（遍历），对于数组`[3，2，4]`和目标值`6`：

```
（1）取3，此时另一个加数应该为6-3=3，下一步则在剩下的元素中寻找是否有3，有则返回两个3的下标，没有则继续取下一个元素；
（2）取2，此时另一个加数应该为6-2=4，下一步则在剩下的元素中寻找是否有4，有则返回2和4的下标，即[1,2]
（3）取4，此时另一个加数应该为6-4=2，下一步则在剩下的元素中寻找是否有2，有则返回4和2的下标，即[2,1]
```

因为题目强调了只存在一个答案，所以在解题时只需要存在一个解即可返回结果；同时根据上述过程可以看到存在重复的情况，即2和4的组合一样，只不过换了位置。因此，遍历当前元素的时候就不用再从该元素之前的元素中找答案了。

使用人工推导的思维打开解题思路后，剩下的过程即将上述解题步骤中的自然语言转换为代码：

```python
class Solution(object):
  def TwoSum(self,nums,target):
    '''
    type nums: List[int]
    type target: int
    rtype List[int]
    '''
    #按照解题思路，首先我们要遍历整个列表
    for i in range(len(nums)):
      #当取nums[i]的时候，另一个加数应该为：
      res = target - nums[i]
      #下一步即在剩下来的元素中找是否有另一个加数
      if res in nums[i+1:]:
        #如果存在即可返回两个加数的下标，结束程序
        #需要强调的是，为了避免重复，另一个加数总会在当前取的加数之后的元素中去找，因此对nums进行了切片，此时的res是从nums中的第i+1个元素开始匹配。也就是说，原始列表的第i+1个元素在切片后的列表nums[i+1:]中为第0个元素
        #因此在获取res在nums[i+1:]中国的索引后还需要再加上i+1，才是其在原始列表中的下标
        return[i,nums[i+1:].index(res)+i+1]
      
#用户自行输入数组和目标值用于测试
input_nums = input("请输入整数数组：")
input_target = input("请输入整数目标值：")

#需要将输入的字符串转换为整数列表，输入的目标值转换为整数目标值
test_nums = [int(num.strip())for num in input_nums.split(',')]
test_target = int(input_target)

#创建test测试对象并调用TwoSum方法
test = Solution()
result = test.TwoSum(test_nums,test_target)
print(result)
```



### 1.3 基础知识汇总

- [Python中range函数的用法](https://www.runoob.com/python/python-func-range.html)
- [Python中List index()方法](https://www.runoob.com/python/att-list-index.html)
- [Python中for循环语句](https://www.runoob.com/python/python-for-loop.html)
- [Python中split()方法](https://www.runoob.com/python/att-string-split.html)
- [Python中strip()方法](https://www.runoob.com/python/att-string-strip.html)