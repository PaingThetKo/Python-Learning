nums = [1,2,3,4,5,6,7,8,9,10]

#      original way
# evenNum = []
# for num in nums:
#     if (num%2)==0:
#         evenNum.append(num)
# print(evenNum)

#      comprehension way
# nums = [num for num in nums if (num%2)==0]
# print(nums)

#      filtering way
def filterFunction(num):
    return (num%2)==0
nums = list(filter(filterFunction,nums))
print(nums)