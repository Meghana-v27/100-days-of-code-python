# ==========================================================
# Problem 1: Count Even Numbers in a List
# ==========================================================

lis1=[2,5,8,11,14]
count=0
for num in lis1:
    if num%2==0:
        count+=1
print(count)


# ==========================================================
# Problem 2: Find the Largest Element in a List
# ==========================================================

lis1=[12,45,7,89,23]
largest=lis1[0]
for num in lis1:
    if num>largest:
        largest=num
print(largest)


# ==========================================================
# Problem 3: Find the Smallest Element in a List
# ==========================================================

list1=[12,45,7,89,23]
smallest=list1[0]
for num in list1:
    if num<smallest:
        smallest=num
print(smallest)


# ==========================================================
# Problem 4: Reverse a List Without Using Built-in Methods
# ==========================================================

list1=[1,2,3,4,5]
rev=[]
for num in list1:
    rev=[num]+rev
print(rev)


# ==========================================================
# Problem 5: Calculate the Sum of List Elements
# ==========================================================

lis1=[4,8,10]
tot=0
for num in lis1:
    tot+=num
print(tot)


# ==========================================================
# Problem 6: Count Occurrences of a Target Element
# ==========================================================

list1=[1,2,3,2,4,2]
target=2
count=0
for num in list1:
    if num==target:
        count+=1
print(count)


# ==========================================================
# Problem 7: Remove Duplicate Elements from a List
# ==========================================================

list1=[1,2,2,3,1,4]
uniq=[]
for num in list1:
    if num not in uniq:
        uniq+=[num]
print(uniq)


# ==========================================================
# Problem 8: Calculate the Average of List Elements
# ==========================================================

def avg(*list1):
    tot=0
    for num in list1:
        tot+=num
    average=tot/len(list1)
    return average

list1=[10,20,30,40]
print(avg(*list1))


# ==========================================================
# Problem 9: Find the Square of Each List Element
# ==========================================================

def squares(*list1):
    square=[]
    indx=0
    while indx<len(list1):
        square+=[list1[indx]**2]
        indx+=1
    return square

list1=[2,3,4,5]
print(squares(*list1))


# ==========================================================
# Problem 10: Count Positive Numbers in a List
# ==========================================================

def positiveCount(*list1):
    count=0
    for num in list1:
        if num>0:
            count+=1
    return count

print(positiveCount(-2,5,0,7,-1,9))
