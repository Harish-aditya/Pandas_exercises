# # from cmath import sqrt
# import math

# x = input()
# x = x.split(" ")
# y = int(x[0])*int(x[1])
# print(y)
# # if math.sqrt(y) is float:
# #     print(math.sqrt(y))
# #     print("no")
# # else:
# #     print(math.sqrt(y))
# #     print("yes")
# if x[0] == x[1]:
#     print('yes')
# else:
#     print('no')
# x = input()
# x = x.split(" ")
# y = int(x[0])**int(x[1])
# print(y)
# x = input()
# x = x.split(" ")
# # Python program to print all
# # prime number in an interval

# def prime(x, y):
# 	prime_list = []
# 	for i in range(x, y+1):
# 		if i == 0 or i == 1:
# 			continue
# 		else:
# 			for j in range(2, int(i/2)+1):
# 				if i % j == 0:
# 					break
# 			else:
# 				prime_list.append(i)
# 	return prime_list

# # Driver program
# starting_range = int(x[0])
# ending_range = int(x[1])
# lst = prime(starting_range, ending_range)
# if len(lst) == 0:
# 	print("There are no prime numbers in this range")
# else:
# 	print(len(lst))
x = input()
x = x.split(" ")
print(x)
x = [int(i) for i in x]
print(x)
print(type(x[0]))
print((x[0]*x[1])/2)
