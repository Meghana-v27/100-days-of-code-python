# 1. Sum of First and Last Digit
# Task: Given a number, find the sum of its first digit and last digit.
# Example Input: Number = 58392
# Example Output: First digit = 5, Last digit = 2, Sum = 7
# num=58392
# lastdigit=num%10
# while num>=10:
#     num//=10
# firstdigit=num
# print(f'First digit = {firstdigit}, Last digit = {lastdigit}, Sum = {firstdigit+lastdigit}')

#-------------------------------------------------------
# 2. Count Digits Greater Than 5
# Task: Count digits in a number that are greater than 5.
# Example Input: Number = 836921
# Example Output: Digits greater than 5 = 4
# num=836921
# target=5
# count=0
# while num>0:
#     digit=num%10
#     if digit>target:
#         count+=1
#     num//=10
# print(f'Digits greater than {target} = {count}')

#---------------------------------------------------
# 3. Product of Digits at Odd Positions
# Task: Find product of digits present at odd positions from right side.
# Example Input: Number = 58294
# Example Output: Product = 64
# number=58294
# position=0
# product=1
# while number>0:
#     position+=1
#     digit=number%10
#     if position%2==1:
#         product*=digit
#     number//=10
# print(f'Product = {product}')
#--------------------------------------------------------
# 4. Largest Digit Difference
# Task: Find difference between largest and smallest digit.
# Example Input: Number = 58392
# Example Output: Largest = 9, Smallest = 2, Difference = 7
# number=58392
# largest=0
# smallest=9
# while number>0:
#     digit=number%10
#     if digit>largest:
#         largest=digit
#     if digit<smallest:
#         smallest=digit
#     number//=10
# difference=largest-smallest
# print(f'Largest = {largest}, Smallest = {smallest}, Difference = {difference}')
# #-----------------------------------
# 5.Count Even and Odd Digits
# Task: Count even and odd digits in a number.
# Example Input: Number = 58392
# Example Output: Even digits = 2, Odd digits = 3
# number=58392
# position=1
# even=0
# odd=0
# while number>0:
#     if position%2==1:
#         odd+=1
#     else:
#         even+=1
#     number//=10
#     position+=1
# print(f'Even digits = {even}, Odd digits = {odd}')
#--------------------------------------
# 6. Reverse Number Without Changing Middle Digit
# Task: Reverse first and last digits while keeping middle digits unchanged.
# Example Input: Number = 12345
# Example Output: Result = 52341
# number=12345
# temp=number
# count=0
# result=0
# while number>0:
#     count+=1
#     number//=10
# pow=10**(count-1)
# first=temp//pow
# last=temp%10
# mid=(temp%pow)//10
# result=last*pow+mid*10+first
# print(f'Result = {result}')
#-----------------------------------------
# 7. Digit Sum Until Single Digit
# Task: Add digits repeatedly until one digit remains.
# Example Input: Number = 9876
# Example Output: Final Result = 3
# number=9876
# sum,final_sum=0,0
# while number>0:
#     digit=number%10
#     sum+=digit
#     number//=10
# while sum>0:
#     digit=sum%10
#     final_sum+=digit
#     sum//=10
# print(f'Final Result = {final_sum}')
#------------------------------------------
# 8. Second Largest Digit
# Task: Find the second largest digit in a number.
# Example Input: Number = 58392
# Example Output: Largest = 9, Second largest = 8
# number=58392
# t=number
# largest=0
# secLargest=0
# position=0
# while number>0:
#     position+=1
#     digit=number%10
#     if digit>largest:
#         largest=digit
#         pos=position
#     number//=10
# temp=t-largest*(10**(pos-1))
# while temp>0:
#     digit=temp%10
#     if digit>secLargest:
#         secLargest=digit
#     temp//=10
# print(f'Largest = {largest}, Second largest = {secLargest}')
#------------------------------------------------------------
# 9. Replace Zero Digits
# Task: Replace all zero digits with 9.
# Example Input: Number = 102030
# Example Output: Result = 192939
# number=102030
# temp=number
# pos,res,count=0,0,0
# while temp>0:
#     count+=1
#     temp//=10
# while number>0 and pos<count:
#     digit=number%10
#     if digit%10==0:
#         res+=9*(10**pos)
#     else:
#         res+=digit*(10**pos)
#     number//=10
#     pos+=1
# print(res)
#---------------------------------------------
# 10. Digit Position Finder
# Task: Find position of a digit in a number from right side.
# Example Input: Number = 58392, Digit = 3
# Example Output: Position = 3
# number=58392
# Digit=3
# pos=0
# while number>0:
#     rem=number%10
#     pos+=1
#     if rem==Digit:
#         print(f'Position = {pos}')
#         break
#     number//=10
#--------------------------------------------------------------
