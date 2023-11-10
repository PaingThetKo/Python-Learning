# normal return function 
# def add(n1,n2):
#     return n1+n2
# print(add(4,5))

# lambda function
# add = lambda n1,n2: n1+n2
# print(add(4,5))


# # filtering concept 
# nums = [1,2,3,4,5,6,7,8,9]
# def filterfuncion(num):
#     return (num%2)==0
# nums = list(filter(filterfuncion,nums))
# print(nums)

# filterig concept with lambda function
nums = [1,2,3,4,5,6,7,8,9]
evenNum = list (filter(lambda num:(num%2)==0,nums))
print(evenNum)