nums=[2,7,11,15]
target = 9

def twoSum(self, nums, target):
    num_map ={2:0}
    for i ,num in enumerate(nums):
            print(i)
            print(num)
            complement = target - num
            if complement in num_map:
             return [num_map[complement],i]
             num_map[num]=i
             return []
        