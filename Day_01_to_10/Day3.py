# #problem1
# num=int(input("Enter a number:"))
# factor=1
# print("factors are :")
# while factor<=num:
#     if num%factor==0:
#         print(factor,end=" ")
#     factor+=1
#--------------------------------------------------------
# #problem2
# num=int(input("Enter a number:"))
# factor=1
# count=0
# while factor<=num:
#     if num%factor==0:
#         count+=1
#     factor+=1
# print("Total Factors =",count)
#-----------------------------------------------------------
# #problem3
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# factor=1
# print("Common Factors:")
# while factor<=num1 and factor<=num2:
#     if num1%factor==0:
#         if num2%factor==0:
#             print(factor,end=" ")
#     factor+=1
#----------------------------------------------------------------------
# #Problem4
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# factor=1
# hcf=1
# while factor<=num1 and factor<=num2:
#     if num1%factor==0 and num2%factor==0:
#             curr_factor=factor
#     if curr_factor>hcf:
#         hcf=curr_factor
#     factor+=1
# print("HCF =",hcf)
#-----------------------------------------------------------------------
# #problem5
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# factor=1
# gcd=1
# while factor<=num1 and factor<=num2:
#     if num1%factor==0 and num2%factor==0:
#             gcd=factor
#     factor+=1
# lcm=(num1*num2)//gcd
# print("LCM =",lcm)
#-------------------------------------------------------------------------
#problem6
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# factor=1
# hcf=1
# while factor<=num1 and factor<=num2:
#     if num1%factor==0 and num2%factor==0:
#             curr_factor=factor
#     if curr_factor>hcf:
#         hcf=curr_factor
#     factor+=1
# if hcf==1:
#     print("Coprime Numbers")
# else:
#     print("Not Coprime Numbers")

#-----------------------------------------------------------------------
#problem7
# num=int(input("Enter a number:"))
# factor=1
# sum=0
# while factor<=num:
#     if num%factor==0:
#         sum+=factor
#     factor+=1
# sum-=num
# if sum==num:
#     print("Perfect Number")
# else:
#     print("Not a perfect Number")
#---------------------------------------------------------------------
# #problem8
# num=int(input("Enter a number:"))
# factor=1
# largest=1
# while factor<=num:
#     if num%factor==0:
#         curr=factor
#     if curr>largest and curr!=num:
#         largest=curr
#     factor+=1
# print("Greatest Factor = ",largest)
#---------------------------------------------------------------------------
#problem9
# num1=int(input("Enter first machine:"))
# num2=int(input("Enter second machine:"))
# factor=1
# gcd=1
# while factor<=num1 and factor<=num2:
#     if num1%factor==0 and num2%factor==0:
#             gcd=factor
#     factor+=1
# lcm=(num1*num2)//gcd
# print(lcm,"Minutes")
#-----------------------------------------------------------------------------------
#problem10
# num1=int(input("Enter  number of chocholates:"))
# num2=int(input("Enter  number of biscuits:"))
# factor=1
# hcf=1
# while factor<=num1 and factor<=num2:
#     if num1%factor==0 and num2%factor==0:
#             curr_factor=factor
#     if curr_factor>hcf:
#         hcf=curr_factor
#     factor+=1
# print(hcf,"Gift Boxes")
