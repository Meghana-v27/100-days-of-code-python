def addition(a,b):
    sum=a+b
    return sum
def subraction(a,b):
    diff=a-b
    return diff
def multipication(a,b):
    product=a*b
    return product
def division(a,b):
    res=a/b
    return res
def Modulus(a,b):
    remainder=a%b
    return remainder 
def floor_division(a,b):
    quotient=a//b
    return quotient
def power(a,b):
    pow=a**b
    return pow
def clear_ans():
    ans=0
    return ans
def show_ans(ans):
    return ans
def Mini_Calculator():
    print('''Menu:
1.Addition 2.Subraction 3.Multipication 4.Division 5.Modulus 
6.Floor Division 7.Power  8.ClearAns 9.Show Ans 10.Exit''')
    exit=1
    ans=0
    while exit!=0 :
        choice=int(input("Enter your choice:"))
        if choice==10:
                break
        elif choice>10:
            print("Invalid Choice")
            continue
        if choice==9:
            print(ans)
            continue
        if choice==8:
            ans=clear_ans()
        previous=int(input("want to work  on previous output yes(1) no(0):"))
        if previous==0:
            num1,num2=list(map(int,input("Enter numbers:").split()))
        else:
            num1=ans
            num2=int(input("Enter second number:"))
        if choice==1:
            ans=addition(num1,num2)
        if choice==2:
            ans=subraction(num1,num2)
        if choice==3:
            ans=multipication(num1,num2)
        if choice==4:
            ans=division(num1,num2)
        if choice==5:
            ans=Modulus(num1,num2)
        if choice==6:
            ans=floor_division(num1,num2)
        if choice==7:
            ans=power(num1,num2)
        print(ans)
        continue
Mini_Calculator()