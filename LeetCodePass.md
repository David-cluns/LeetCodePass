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



## 2 移动零

### 2.1 题目描述

> 给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。
>
> **请注意** ，必须在不复制数组的情况下原地对数组进行操作。
>
> **示例 1:**
>
> ```
> 输入: nums = [0,1,0,3,12]
> 输出: [1,3,12,0,0]
> ```
>
> **示例 2:**
>
> ```
> 输入: nums = [0]
> 输出: [0]
> ```



### 2.2 题目解答

#### 2.2.1 引入新数组

该方法的基本思路为：遍历输入的数组，记住非零元素的下标，将非零元素按顺序放置在新数组中，最后将剩下的零元素加入新数组的末尾。

```python
class Solution(Object):
  def moveZeroes(self,nums):
    #定义一个空的新数组
    result = []
    zero_count = 0
    #遍历输入的数组，找出非零元素，按顺序存入新数组
    for i in range(len(nums)):
      if nums[i] !=0:
        result.append(nums[i])
      else:
        zero_count += 1
    
    result.expend([0]*zero_count)
    return result
  
test = Solution()
nums = input("请输入数组：")
test_nums = [int(nums.strip()) for num in nums.slip(',')]
results = test.moveZeroes(test_nums)
print(result)
```



#### 2.2.2 双指针——两次遍历

该方法的详细思路参考LeetCode题解：[动画演示283.移动零](https://leetcode.cn/problems/move-zeroes/solutions/90229/dong-hua-yan-shi-283yi-dong-ling-by-wang_ni_ma/?envType=study-plan-v2&envId=top-100-liked)

> 核心观点是：该方式创建了两个指针 `i` 和 `j`,第一次遍历的时候，由指针`j`记录输入数组中的非零元素。即遍历的时候每遇到一个非零元素就将其往数组左边挪，第一次遍历结束的时候，指针`j`元素刚好指向的是最后一个非零元素的下一个元素。
>
> 这样在第二次遍历的时候，只需要将从`j`开始到数组结束后的元素均置为0即可。

```python
class Solution(Object):
  def moveZeroes(self,nums):
    j = 0
    for i in range(len(nums)):
      if nums[i]:
        nums[j] = nums[i]
        j += 1
    for i in range(j,len(nums)):
      nums[i] = 0
      
    return nums

test = Solution()
nums = input("请输入数组：")
test_nums = eval(nums)
results = test.moveZeroes(test_nums)
print(resultes)
```



#### 2.2.3双指针——一次遍历

该方法的详细思路参考LeetCode题解：[动画演示283.移动零](https://leetcode.cn/problems/move-zeroes/solutions/90229/dong-hua-yan-shi-283yi-dong-ling-by-wang_ni_ma/?envType=study-plan-v2&envId=top-100-liked)

> 核心观点是：参考快速排序的思想，以`0`作为中间点，不等于`0`的元素均放置在`0`的左边，等于`0`的元素均放置在其右边。具体的实现思路就是利用指针 `i` 和 指针`j`，遍历输入数组，只要`nums[i]`!=0，就将其与`nums[j]`交换位置。

```python
class Solution(object):
  def moveZeroes(self,nums):
    j = 0
    for i in range(len(nums)):
      if nums[i]:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        j += 1
    return nums
  
test = Solution()
nums = input("请输入数组：")
test_nums = eval(nums)
result = test.moveZeroes3(test_nums)
print(result)
```



### 2.3 基础知识汇总

- [python extend()与append()的区别](https://blog.csdn.net/weixin_38145317/article/details/89485983)
- [Python eval() 函数](https://www.runoob.com/python/python-func-eval.html)



## 3 相交链表

### 3.1 题目描述

![getIntersectionNode](./img/getIntersectionNode.jpg)

### 3.2 题目解答

本题解题思路参考LeetCode题解：[【相交链表】五种解法～](https://leetcode.cn/problems/intersection-of-two-linked-lists/solutions/887414/xiang-jiao-lian-biao-wu-chong-jie-fa-by-j73p5/?envType=study-plan-v2&envId=top-100-liked)

想要解答该题，首先需要了解相交链表的概念。这里给出查阅的两个解释：

**解释一**：[图解LeetCode_160.相交链表](https://cloud.tencent.com/developer/article/2286581)

![intersection](./img/intersection.jpg)

**解释二：**来自chatGPT4.0

> 相交链表是指两个单链表在某个节点处“相交”，并且从该节点**之后的部分完全共享**。也就是说，它们从这个相交点开始拥有相同的节点。
>
> #### 如何判断两个链表是否相交？
>
> 1. **计算长度**：我们可以先分别遍历两个链表，计算它们的长度。
> 2. **对齐指针**：因为两个链表相交后的部分是相同的，所以我们可以将较长链表的指针向前移动，使两个链表的指针位于相同的剩余长度上。
> 3. **同步遍历**：然后我们同时遍历两个链表，逐个比较它们的节点。如果两个指针指向同一个节点，则表示找到相交节点。如果遍历结束都没有发现相交点，则表示它们没有相交。

了解了相交链表的概念后，再来观察此题，题目已经说明了给出的为两个单链表，所以要么这两个链表相交（及相交节点后的部分完全相同），要么为平行链表，不可能为解释一中的情况2。所以，只需要确认两个单链表是否有相同的节点值即可。

```python
class Solution(object):
  def getIntersectionNode(self,headA,headB):
    s = set()
    p,q = headA,headB
    #将链表A存入
    while p:
      s.add(p)
      p = p.next
      
    while q:
      if q in s:
        return q
      q = q.next
    return None
```



## 4. 反转链表

### 4.1 题目描述

![reverselist](./img/reverselist.png)

### 4.2 题目解答

本题的解题思路参考[《代码随想录》：帮你拿下反转链表](https://www.bilibili.com/video/BV1nB4y1i7eL/?vd_source=63ae45ff293024cc1925b41a2202a3a6)

该视频提供了两种解题思路，个人认为双指针的逻辑相较于递归解法更加清晰，也更易懂。

#### 4.2.1 双指针

所谓双指针，顾名思义就是引入了两个指针：cur指针初始化为head指针，pre指针为空指针。

为了便于理解，我们以示例1的图为参考，此时cur指针相当于1，正向情况下它指向它的后一个节点2。而为了使链表反转，需要让1指向他的前一个节点，即定义的pre指针，翻译成代码，也就是cur.next = pre。但是需要注意的是，在改变链表方向前，不能丢失后面的节点，所以应该先让一个临时指针存下后面的节点，再进行反转，即tmp = cur.next。

这样就完成了一个节点的反转，接下来只需要把pre指针和cur指针向后移动，重复上述步骤即可。不过，这里还需要注意，需要先移动pre指针，再移动cur指针。否则，pre指针无法找到cur指针的原始位置。当pre指针移动到尾节点时，链表才完成了整体的反转。此时，cur指针脱离了链表，成为了空指针。

```python
def reverseList(self, head):
  #初始化指针
  cur = head
  pre = None
  
  #当cur指针非空时，一直进行反转操作
  while cur:
    tmp = cur.next #先用tmp指针保存后面的节点
    cur.next = pre #再反转链表方向
    # 反转完成后，先移动pre指针,再移动cur指针
    pre = cur
    cur = tmp
  
  return pre
```



#### 4.2.2 递归

实际上，递归的方式完全是按照双指针的逻辑进行改写的，只不过把循环变成了迭代

```python
def reverseList(self, head):
  #把双指针的思路转换为一个递归函数
  def reverse(cur, pre)：
  	if cur == None:
      return pre
    tmp = cur.next
    cur.next = pre
    
    #把移动的步骤转换为递归
    return reverse(tmp,cur)
  
  #主体函数只需要调用递归函数即可
  return reverse(head, None)
```

