def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num not in dic:
            dic[target - num] = i
        else:
            return [dic[num], i]