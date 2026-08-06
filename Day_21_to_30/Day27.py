# # 1. Rotate Digits Left
# # Definition: Left rotation moves the first digit to the end.
# # Task: Rotate the given number one position to the left.
# # Example Input: 12345
# # Example Output: 23451
# num=int(input('Enter a number :'))
# temp=num
# c=0
# while temp>0:
#     c+=1
#     temp//=10
# first=num//(10**(c-1))
# n=num%(10**(c-1))
# rotated=n*10+first
# print(rotated)



# # 2. Rotate Digits Right
# # Definition: Right rotation moves the last digit to the beginning.
# # Task: Rotate the given number one position to the right.
# # Example Input: 12345
# # Example Output: 51234
# num=int(input('Enter a number :'))
# temp=num
# c=0
# while temp>0:
#     c+=1
#     temp//=10
# rem=num//10
# n=num%10
# rotated=n*(10**(c-1))+rem
# print(rotated)



# # 3. Swap First and Last Digits
# # Definition: Exchange the first and last digits.
# # Task: Print the modified number.
# # Example Input: 58391
# # Example Output: 18395
# num=int(input('Enter a number :'))
# temp=num
# c=0
# while temp>0:
#     c+=1
#     temp//=10
# first=num%10
# pos=10**(c-1)
# n=num//(pos)
# updated_n=(num-(n*(pos)))//10
# rotated=first*(pos)+updated_n*10+n
# print(rotated)


# 4. Replace Every Even Digit with 0
# Definition: Every even digit becomes 0.
# Task: Transform the number.
# Example Input: 482763
# Example Output: 003703
# num=int(input('Enter a number:'))
# temp=num
# c=0
# while temp!=0:
#     c+=1
#     temp//=10
# replaced_nums=[0]*c
# indx=c-1
# while num>0 and 0<=indx<c:
#     digit=num%10
#     if digit%2!=0:
#         replaced_nums[indx]+=digit
#     num//=10
#     indx-=1
# for i in replaced_nums:
#     print(i,end='')


# # 5. Replace Every Odd Digit with 9
# # Definition: Every odd digit becomes 9.
# # Task: Transform the number.
# # Example Input: 482763
# # Example Output: 492769
# num=int(input('Enter a number:'))
# temp=num
# c=0
# while temp!=0:
#     c+=1
#     temp//=10
# replaced_nums=[0]*c
# indx=c-1
# while num>0 and 0<=indx<c:
#     digit=num%10
#     if digit%2==0:
#         replaced_nums[indx]+=digit
#     else:
#         replaced_nums[indx]+=9
#     num//=10
#     indx-=1
# for i in replaced_nums:
#     print(i,end='')


# # 6. Reverse Only Even Digits
# # Definition: Reverse only even digits, keep odd digits fixed.
# # Task: Print transformed number.
# # Example Input: 284673
# # Example Output: 684273
# num=int(input("Enter a number :"))
# temp=num
# rev=0
# odds=0
# c=0
# while temp>0:
#     if (temp%10)%2==0:
#         rev=rev*10+temp%10
#     else:
#         odds=(temp%10)*(10**c)+odds
#         c+=1
#     temp//=10
# print(rev*(10**c)+odds)



# # 7. Reverse Only Odd Digits
# # Definition: Reverse only odd digits, keep even digits fixed.
# # Task: Print transformed number.
# # Example Input: 583921
# # Example Output: 123985
# num=int(input("Enter a number :"))
# temp=num
# rev=0
# evens=0
# c=0
# while temp>0:
#     if (temp%10)%2!=0:
#         rev=rev*10+temp%10
#         c+=1
#     temp//=10
# temp=num
# pos=1
# result=0
# while temp>0:
#     digit=temp%10
#     if digit%2==0:
#         result+=digit*pos
#     else:
#         result+=(rev%10)*pos
#         rev//=10
#     pos*=10
#     temp//=10
# print(result)


# # 8. Move All Zeros to the Front
# # Definition: Move every zero to the beginning.
# # Task: Transform the number.
# # Example Input: 5020301
# # Example Output: 0005231
# num=int(input('Enter a number:'))
# temp=num
# pos=1
# zeros_c=0
# res=0
# while temp>0:
#     digit=temp%10
#     if digit==0:
#         zeros_c+=1
#     else:
#         res+=digit*pos
#         pos*=10
#     temp//=10
# print(zeros_c*'0',end='')
# print(res)




# # 9. Move All Zeros to the End
# # Definition: Move every zero to the end.
# # Task: Transform the number.
# # Example Input: 5020301
# # Example Output: 5231000
# num=int(input('Enter a number:'))
# temp=num
# pos=1
# zeros_c=0
# res=0
# while temp>0:
#     digit=temp%10
#     if digit==0:
#         zeros_c+=1
#     else:
#         res+=digit*pos
#         pos*=10
#     temp//=10
# print(res*(10**zeros_c))



# # 10. Remove Every Alternate Digit
# # Definition: Keep only the 1st, 3rd, 5th... digits.
# # Task: Print resulting number.
# # Example Input: 98765432
# # Example Output: 9753
# num=int(input('Enter a number:'))
# temp=num
# count=0
# res=0
# pos=1
# while temp>0:
#     count+=1
#     temp//=10
# while num>0 and count>0:
#     digit=num%10
#     if count%2!=0:
#         res+=digit*pos
#         pos*=10
#     count-=1
#     num//=10
# print(res)





# # 11. Duplicate Every Digit
# # Definition: Every digit appears twice consecutively.
# # Task: Print transformed number.
# # Example Input: 483
# # Example Output: 448833
# num=int(input('Enter a number:'))
# res=0
# pos=1
# while num>0:
#     digit=num%10
#     res=((digit*10)+digit)*pos+res
#     pos*=100
#     num//=10
# print(res)



# # 12. Insert 0 Between Every Pair of Digits
# # Definition: Insert one zero between consecutive digits.
# # Task: Transform the number.
# # Example Input: 5678
# # Example Output: 5060708
# num=int(input('Enter a number:'))
# res=0
# temp=num
# c=0
# while temp>0:
#     c+=1
#     temp//=10
# while num>0:
#     pos=(10**(c-1))
#     digit=num//pos
#     if c==1:
#         res=res*10+(digit)
#     else:
#         res=(res*100+(digit*10))
#     num-=digit*pos
#     c-=1
# print(f'result : {res}')


# # 13. Mirror the Number
# # Definition: Append the reverse to itself.
# # Task: Print mirrored number.
# # Example Input: 357
# # Example Output: 357753
# num=int(input('Enter a number:'))
# temp=num
# rev,c=0,0
# while temp>0:
#     rev=rev*10+temp%10
#     temp//=10
#     c+=1
# print(num*(10**c)+rev)



# # 14. Compress Consecutive Digits
# # Definition: Replace repeated consecutive digits with digit+count.
# # Task: Compress the number.
# # Example Input: 11122333344
# # Example Output: 13224342
# num=int(input('Enter a number:'))
# res=0
# while num>0:
#     res=res*10+num%10
#     num//=10
# prev=res%10
# res=res//10
# count=1
# while res>0:
#     digit=res%10
#     if digit==prev:
#         count+=1
#     else:
#         print(prev,end='')
#         print(count,end='')
#         prev=digit
#         count=1
#     res=res//10
# print(prev,end='')
# print(count)


# # 15. Expand the Number
# # Definition: Write each digit according to its place value.
# # Task: Print expanded form.
# # Example Input: 5078
# # Example Output: 5000 + 70 + 8
# num=int(input('Enter a number:'))
# temp=num
# c=0
# while temp>0:
#     c+=1
#     temp//=10
# while num>0 and c>0:
#     pos=10**(c-1)
#     digit=num//pos
#     if digit>0 and c>1:
#         expand=(digit)*pos
#         print(expand,end='+')
#     elif c==1 and digit>0:
#         expand=(digit)*pos
#         print(expand)
#     c-=1
#     num=num%pos




# # 16. Print Digits in Wave Order
# # Definition: First,last,second,second-last...
# # Task: Rearrange digits.
# # Example Input: 123456
# # Example Output: 162534
# num=int(input('Enter a number:'))
# temp=num
# c=0
# res=0
# while temp>0:
#     c+=1
#     temp//=10
# while num>0 and c>0:
#     pos=10**(c-1)
#     first=num//pos
#     last=num%10
#     res=res*10+first
#     res=res*10+last
#     num=num%pos
#     num//=10
#     c-=2
# print(res)



# # 17. Reverse Digits in Pairs
# # Definition: Reverse every two consecutive digits.
# # Task: Transform the number.
# # Example Input: 123456
# # Example Output: 214365
# num=int(input('Enter a number:'))
# temp=num
# c=0
# res=0
# while temp>0:
#     c+=1
#     temp//=10
# if c%2==0:
#     while num>0 and c>0:
#         x=c-1
#         pos=10**x
#         digit=num//pos
#         if x%2!=0:
#             res=res*100+digit
#         else:
#             res=digit*10+res
#         num=num%pos
#         c-=1
#     print(res)



# # 18. Replace Every Digit with Its Complement to 9
# # Definition: Replace d with 9-d.
# # Task: Transform the number.
# # Example Input: 2845
# # Example Output: 7154
# num=int(input('Enter a number:'))
# temp=num
# c=0
# res=0
# while temp>0:
#     c+=1
#     temp//=10
# while num>0 and c>0:
#     pos=10**(c-1)
#     digit=num//pos
#     res=res*10+(9-digit)
#     num=num%pos
#     c-=1
# print(res)




# # 19. Sort Even and Odd Digits Separately
# # Definition: Sort evens among evens and odds among odds.
# # Task: Print modified number.
# # Example Input: 86427531
# # Example Output: 24613578
# num=int(input('Enter a number:'))
# temp=num
# even=0
# odd=0
# while temp>0:
#     digit=temp%10
#     if digit%2==0:
#         even=even*10+digit
#     else:
#         odd=odd*10+digit
#     temp//=10
# for i in range(0,10,2):
#     temp=even
#     while temp>0:
#         digit=temp%10
#         if i==digit:
#             print(digit,end='')
#         temp//=10
# for i in range(1,10,2):
#     temp=odd
#     while temp>0:
#         digit=temp%10
#         if digit==i:
#             print(digit,end='')
#         temp//=10



# # 20. Interleave Two Halves
# # Definition: Split into equal halves and alternate digits.
# # Task: Rearrange digits.
# # Example Input: 12345678
# # Example Output: 15263748
# num=int(input('Enter a number:'))
# temp=num
# onehalf=0
# c=0
# sechalf=0
# while temp>0:
#     c+=1
#     temp//=10
# count=0
# p=c-1
# while num>0 and count<(c//2):
#     pos=10**p
#     digit=num//pos
#     onehalf=onehalf*10+digit
#     num%=pos
#     count+=1
#     p-=1
# sechalf=num
# while onehalf>0 and sechalf>0 and p>=0:
#     pos=10**p
#     digit=onehalf//pos
#     print(digit,end='')
#     digit2=sechalf//pos
#     print(digit2,end='')
#     onehalf%=pos
#     sechalf%=pos
#     p-=1
