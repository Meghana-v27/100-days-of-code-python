#Electricity bill calculator
units=int(input("Enter units:"))
while units>0:
    if units>100:
        cost=100*5
        units-=100
    if units>100:
        cost+=100*7
        units-=100
    if units>0:
        cost+=units*10
        units=0
print(cost)
#------Armstrong Number Checker----------------------------------
num=int(input("Enter a number:"))
temp=num
count=0
number=0
while num>0:
    if num%10!=0:
        count+=1
    num//=10
num=temp
while num>0:
    rem=num%10
    number+=rem**count
    num//=10
if temp==number:
    print(f"{temp} is Amstrong number")
else:
    print(f"{temp} is not Amstrong Number")
#-------------------------------------Palindrome Number Checker--------------------------------------------
num=int(input("Enter a number:"))
temp=num
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num//=10
if temp==reverse:
    print("Palindrome number")
else:
    print("Not a plaindrome number")
#-------------------------Count Even and Odd Digits---------------
num=int(input("Enter a number:"))
even_count=0
odd_count=0
while num>0:
    n=num%10
    if n%2==0:
        even_count+=1
    else:
        odd_count+=1
    num=num//10
print("Even digits =",even_count)
print("Odd digits =",odd_count)
#---------------------------ATM Cash Withdrawal System----------------------------------------------------------
balance=int(input("Enter account balance:"))
withdrawl=int(input("Enter withdrawl amount:"))
if withdrawl%10==0 and withdrawl<=balance:
    print("Transaction Sucessful")
    balance-=withdrawl
    print("Remaining balance=",balance)
else:
    print("Error")
#_--------------------------------------Strong Number Checker-------------------------------------------------------
num=int(input("Enter a number:"))
temp=num
number=0
while num>0:
    rem=num%10
    fact=1
    for i in range(2,rem+1):
        fact=fact*i
    number+=fact
    num//=10    
if temp==number:
    print(f'{temp} is a Strong number')
else:
    print(f"{temp} is not a Strong number")
#--------------------------------------Sum of Squares of N Numbers--------------------------------
n=int(input("Enter n:"))
sum=0
for i in range(1,n+1):
    sum+=i**2
print("sum =",sum)
#-----------------------------------Digit Frequency Counter-----------------------------------------
num=int(input("Enter number:"))
frequency={}
while num>0:
    rem=num%10
    if rem  in frequency:
        frequency[rem]+=1
    else:
        frequency[rem]=1
    num=num//10
for i in frequency:
    print(f'{i} Occurs {frequency[i]} times')
#----------------------Prime Numbers in a Range------------------------------
start=int(input("Enter start number:"))
end=int(input("Enter end number:"))
for num in range(start,end+1):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)
#_------------------Employee Gross Salary & Highest Earner Calculator-------------------------------
emp_count=0
while emp_count<2:
    Gross_sal=0
    highest=0
    h_name=""
    name=input("Enter Name:")
    Basic_sal=int(input("Basic Salary:"))
    experience=int(input("Experience:"))
    hra=(15/100)*Basic_sal
    ta=(10/100)*Basic_sal
    if experience>=5:
        bonus=(20/100)*Basic_sal
    else:
        bonus=(10/100)*Basic_sal
    Gross_sal=Basic_sal+hra+ta+bonus

    emp_count+=1
    if Gross_sal>highest:
        highest=Gross_sal
        h_name=name
    print(name,"Gross Salary =",Gross_sal)
print("Highest Gross Salary Employee:",h_name)
print("Gross Salary =",highest)

        

    
