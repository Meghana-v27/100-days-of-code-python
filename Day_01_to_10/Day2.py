"""
==================================================================
Challenge: #100DaysOfCode - Day 2
Focus: Pure Python Logic, State Variables, and String Parsing
==================================================================
Today I engineered 10 modular data and flow control trackers:
1. Longest Login Streak   2. Password Strength    3. Inventory Restock
4. Theater Seat Monitor   5. Risk Failure Alert   6. Revenue Ledger
7. Data Cap Watchdog     8. Election Calculator  9. Fleet Classifier
10. Array Range Analyzer
==================================================================
"""

# ------------------------------------------------------------------
# Problem 1: Longest Login Streak
# ------------------------------------------------------------------
logins = [1, 1, 0, 1, 1, 1, 0, 1]
curr_count = count = 0

print("--- Problem 1: Longest Streak ---")
for login in logins:
    if login == 1:
        curr_count += 1
    else:
        if curr_count > count:
            count = curr_count
        curr_count = 0
if curr_count > count:
    count = curr_count
print("Longest streak =", count, "\n")


# ------------------------------------------------------------------
# Problem 2: Password Validator
# ------------------------------------------------------------------
password = "Abc123X"
upper_count, lower_count, digits_count = 0, 0, 0

print("--- Problem 2: Password Validator ---")
for ch in password:
    if 'A' <= ch <= 'Z':
        upper_count += 1
    elif 'a' <= ch <= 'z':
        lower_count += 1
    elif '0' <= ch <= '9':
        digits_count += 1

print("Uppercase =", upper_count)
print("Lowercase =", lower_count)
print("Digits =", digits_count)

if upper_count >= 1 and lower_count >= 1 and digits_count >= 1:
    print("Strong Password\n")
else:
    print("Weak Password\n")


# ------------------------------------------------------------------
# Problem 3: Inventory Restock Tracker
# ------------------------------------------------------------------
stock = [25, 5, 0, 18, 3, 40]
count = 0

print("--- Problem 3: Stock Alert ---")
for product in stock:
    if product == 0:
        continue
    if product < 10:
        count += 1
print("Products To Restock =", count, "\n")


# ------------------------------------------------------------------
# Problem 4: Theater Occupancy Engine
# ------------------------------------------------------------------
seats = [1, 0, 1, 1, 0, 0, 1]
index, occupy_count = 0, 0

print("--- Problem 4: Occupancy ---")
while index < len(seats):
    if seats[index] == 1:
        occupy_count += 1
    index += 1
print("Occupied =", occupy_count)
print("Empty =", len(seats) - occupy_count)
print(f"Occupancy = {occupy_count / len(seats) * 100:.2f}%\n")


# ------------------------------------------------------------------
# Problem 5: Risk Failure Monitor (Fixed Consecutive Check)
# ------------------------------------------------------------------
results = ['P', 'P', 'F', 'F', 'F', 'P']
consecutive_fail = 0
failed_flag = False

print("--- Problem 5: Risk Monitor ---")
for result in results:
    if result == 'F':
        consecutive_fail += 1
        if consecutive_fail == 3:
            failed_flag = True
            break
    else:
        consecutive_fail = 0

if failed_flag:
    print("3 Consecutive Failures Found\n")
else:
    print("System Secure (No 3 consecutive failures)\n")


# ------------------------------------------------------------------
# Problem 6: Revenue Ledger
# ------------------------------------------------------------------
orders = [500, 800, -500, 1000, -800]
sales = returns = 0

print("--- Problem 6: Ledger ---")
for order in orders:
    if order > 0:
        sales += order
    else:
        returns -= order
print("Sales =", sales)
print("Returns =", returns)
print("Net Revenue =", sales - returns, "\n")


# ------------------------------------------------------------------
# Problem 7: Data Cap Watchdog
# ------------------------------------------------------------------
usage = [450, 600, 700, 550]
limit = 2000
index, used = 0, 0

print("--- Problem 7: Data Usage ---")
while index < len(usage):
    used += usage[index]
    if used > limit:
        print("Limit Exceeded on Day", index + 1)
    index += 1
print("Used =", used, "MB\n")


# ------------------------------------------------------------------
# Problem 8: Election Calculator
# ------------------------------------------------------------------
votes = ['A', 'B', 'A', 'C', 'A', 'B', 'A']
Acount = Bcount = Ccount = 0

print("--- Problem 8: Voting ---")
for vote in votes:
    if vote == "A":
        Acount += 1
    elif vote == "B":
        Bcount += 1
    else:
        Ccount += 1
print("A =", Acount)
print("B =", Bcount)
print("C =", Ccount)

if Acount >= Bcount and Acount >= Ccount:
    print("Winner = A\n")
elif Bcount >= Ccount and Bcount >= Acount:
    print("Winner = B\n")
else:
    print("Winner = C\n")


# ------------------------------------------------------------------
# Problem 9: Fleet Classifier
# ------------------------------------------------------------------
vehicles = ['C', 'B', 'C', 'T', 'B', 'C']
cars = bikes = trucks = 0

print("--- Problem 9: Fleet ---")
for vehicle in vehicles:
    if vehicle == "C":
        cars += 1
    elif vehicle == 'B':
        bikes += 1
    else:
        trucks += 1
print(f"Cars = {cars}\nBikes = {bikes}\nTrucks = {trucks}\n")


# ------------------------------------------------------------------
# Problem 10: Array Range Analyzer (Fixed text prints)
# ------------------------------------------------------------------
numbers = [12, 5, 8, 21, 14, 7]
odd_count = 0
max_num = numbers[0]
min_num = numbers[0]

print("--- Problem 10: Statistics ---")
for num in numbers:
    if num % 2 != 0:
        odd_count += 1
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Odd =", odd_count)
print("Even =", len(numbers) - odd_count)
print("Largest =", max_num)
print("Smallest =", min_num)
