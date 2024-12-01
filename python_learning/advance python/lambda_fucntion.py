#lambda function for even numbers
num = [1,2,3,4,5,6,7,8,9]
even_no = list(filter(lambda x: x%2==0 ,num))
print(even_no)

#lambda function for number greater than or equal to 3
num1 = [1,2,3,2,6,7,1]
nums = list(filter(lambda x: x>=3,num1))
print(nums)

#square of number using lambda fucntion
square_num = list(map(lambda x : x**2,num))
print(square_num)

