n=5
for i in range(1,n+1):
    total=0
    for j in range(1,i+1):
        print(j,end="")
        total+=j
        if j<i:
            print("+",end="")
    print("=",total)
# #_----------------------------------------------
# #problrm2
less=0
between=0
greater=0
for i in range(2,11):
    for j in range(1,11):
        p=i*j
        if p<20:
            less+=1
        elif p<=50:
            between+=1
        else:
            greater+=1
print("Less than 20=",less)
print("20 to 50=",between)
print("Greater than 50=",greater)
# #------------------------------------------------------------------
#problem3
marks=[85,70,92,78,88]
for i in range(len(marks)):
    count=0
    for j in range(len(marks)):
        if marks[j]>marks[i]:
            count+=1
    print(marks[i],"->",count)
#_-------------------------------------------------------
#problem4
sales=[500,900,700,1200]
for i in range(len(sales)):
    rank=1
    for j in range(len(sales)):
        if sales[j]>sales[i]:
            rank+=1
    print(sales[i],"-> Rank",rank)
# #---------------------------------------------------------
print()
print()
# #problem5
numbers=[2,5,7,8,3]
sum=10
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==sum and numbers[i]!=numbers[j]:
            print(f"{numbers[i]}+{numbers[j]}")



# #------------------------------------------------------------
# #problem6
numbers=[2,3,4,6,8]
product=24
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]*numbers[j]==product:
            print(f"{numbers[i]} x {numbers[j]}")
# #-----------------------------------------------------------
# # #problem7
matrix=[[10,20,30],[40,50,60],[70,80,90]]
tot=0
for i in matrix:
    for j in i:
        tot+=j
print("Total =",tot)
# #_--------------------------------
# # #problem8
matrix=[[10,20,30],[40,50,60],[70,80,90]]
row=1
for i in matrix:
    tot=0
    for j in i:
        tot+=j
    print("Row",row,"=",tot)
    row+=1
# #_----------------------------------------
# # problem9
teams=['A','B','C','D']
for i in range(len(teams)+1):
    for j in range(i+1,len(teams)):
        print(f'{teams[i]} vs {teams[j]}')
# #------------------------------------------------
matrix=[[10,20,30],[50,60,70],[15,25,35]]
high=0
row=0
for i in range(len(matrix)):
    tot=0
    for j in matrix[i]:
        tot+=j
    if tot>high:
        high=tot
        row=i+1
print("Row",row)
print("Total =",high)
    