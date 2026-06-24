"""
==================================================================
Challenge: #100DaysOfCode - Day 1
Focus: Pure Python Logic, Loops, Conditionals, and State Tracking
==================================================================
Today I built 10 micro-services mimicking real-world business scenarios:
1. Attendance Tracker   2. Banking Ledger     3. Rating Filter
4. Utility Billing      5. E-Commerce Checkout 6. Academic Analyzer
7. ATM Cash Dispenser   8. Smart Cart         9. Sales Auditor
10. Cricket Stats Engine
==================================================================
"""

# ------------------------------------------------------------------
# Problem 1: Attendance Tracker
# ------------------------------------------------------------------
attendance = ['P', 'A', 'P', 'P', 'A', 'P']
count = attendance.count('P')
percentage = (count / len(attendance)) * 100

print("--- Problem 1: Attendance ---")
print(f"Present Days = {count}")
print(f"Attendance percentage = {percentage:.2f}%\n")


# ------------------------------------------------------------------
# Problem 2: Banking Ledger (Fixed Logic)
# ------------------------------------------------------------------
transactions = [5000, -2000, -3000, -4000]
balance = 6000

print("--- Problem 2: Transactions ---")
for transaction in transactions:
    if transaction > 0:
        balance += transaction 
    else:
        if balance >= abs(transaction):
            balance += transaction
        else:
            print(f"Insufficient balance for withdrawal of {abs(transaction)}")
            break
print(f"Final Balance = {balance}\n")


# ------------------------------------------------------------------
# Problem 3: Rating Filter
# ------------------------------------------------------------------
ratings = [5, 4, 0, 3, 5, 0, 4]
valid_ratings = [rate for rate in ratings if rate != 0]
avg = sum(valid_ratings) / len(valid_ratings) if valid_ratings else 0

print("--- Problem 3: Ratings ---")
print(f"Average Rating = {avg:.2f}\n")


# ------------------------------------------------------------------
# Problem 4: Utility Bill Calculator (Fixed Logic)
# ------------------------------------------------------------------
units = [120, 150, 200, 180]
final_bill = 0

print("--- Problem 4: Electricity Bill ---")
for unit in units:
    if unit > 100:
        bill = (100 * 5) + (unit - 100) * 8
    else:
        bill = unit * 5
    final_bill += bill

print(f"Total Bill = {final_bill}\n")


# ------------------------------------------------------------------
# Problem 5: E-Commerce Checkout
# ------------------------------------------------------------------
prices = [500, 1200, 800, 1500]
total = sum(prices)
discount = sum(int(item * 0.10) for item in prices if item > 1000)

print("--- Problem 5: Checkout ---")
print(f"Total Bill = {total}")
print(f"Discount = {discount}")
print(f"Final Bill = {total - discount}\n")


# ------------------------------------------------------------------
# Problem 6: Academic Analyzer
# ------------------------------------------------------------------
marks = [75, 30, 82, 40, 95, 28]
passed = sum(1 for mark in marks if mark > 35)
failed = len(marks) - passed

print("--- Problem 6: Exam Marks ---")
print(f"Passed = {passed}")
print(f"Failed = {failed}\n")


# ------------------------------------------------------------------
# Problem 7: ATM Cash Dispenser (Fixed Infinite Loop)
# ------------------------------------------------------------------
amount = 3700
denominations = [2000, 500, 200, 100]

print("--- Problem 7: ATM Breakdown ---")
for note in denominations:
    if amount >= note:
        count_notes = amount // note
        amount %= note
        print(f"{note} x {count_notes}")
print()


# ------------------------------------------------------------------
# Problem 8: Smart Cart
# ------------------------------------------------------------------
cart = [500, -1, 700, 1200, -1, 300]
total_cart = sum(item for item in cart if item != -1)

print("--- Problem 8: Cart ---")
print(f"Total amount = {total_cart}\n")


# ------------------------------------------------------------------
# Problem 9: Sales Auditor
# ------------------------------------------------------------------
sales = [5000, 7000, -1, 9000, 0, 8000]
total_sales = 0

print("--- Problem 9: Sales ---")
for cost in sales:
    if cost == -1:
        continue
    elif cost > 0:
        total_sales += cost
    else:
        break
print(f"Total Sales = {total_sales}\n")


# ------------------------------------------------------------------
# Problem 10: Cricket Stats Engine
# ------------------------------------------------------------------
runs = [45, 80, 22, 95, 60]
total_runs = sum(runs)
highest_run = max(runs)
avg_runs = total_runs / len(runs)

print("--- Problem 10: Statistics ---")
print(f"Total = {total_runs}")
print(f"Highest = {highest_run}")
print(f"Average = {avg_runs:.2f}\n")
