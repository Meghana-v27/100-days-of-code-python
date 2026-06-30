# Student Grade Checker
def student_grade_checker():
    marks = int(input("Enter marks: "))

    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 35:
        print("Grade: D")
    else:
        print("Fail")


# ATM PIN Verification
def atm_pin_verify():
    actual_pin = 1234
    attempts = 3

    while attempts > 0:
        pin = int(input("Enter PIN: "))

        if pin == actual_pin:
            print("Login Successful")
            break

        attempts -= 1

    else:
        print("Card Blocked")


# Multiplication Table
def multiplication_table():
    num = int(input("Enter a number: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


# Number Guess Validation
def number_guess():
    while True:
        num = int(input("Enter a number: "))

        if 1 <= num <= 100:
            print("Valid Number")
            break
        else:
            print("Invalid Number")


# Pattern Printing
def pattern():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end="")
        print()


# Bus Seat Layout
def bus_seats():
    for row in range(1, 5):
        for col in range(1, 6):
            print(f"R{row}C{col}", end=" ")
        print()


# Restaurant Ordering System
def restaurant():
    print("Menu")
    print("1. Pizza")
    print("2. Burger")
    print("3. Sandwich")
    print("4. Exit")

    count = 0

    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Pizza Ordered")
            count += 1

        elif choice == 2:
            print("Burger Ordered")
            count += 1

        elif choice == 3:
            print("Sandwich Ordered")
            count += 1

        elif choice == 4:
            break

        else:
            print("Invalid Order")

    print("Total Items Ordered =", count)


# Cinema Seat Booking
def cinema_booking():
    booked = []
    booked_seats = 0

    while booked_seats < 5:
        row, col = map(int, input("Enter seat (row,col): ").split(","))

        if 1 <= row <= 5 and 1 <= col <= 6:

            if (row, col) in booked:
                print("Already Booked")

            else:
                print("Seat Booked Successfully")
                booked.append((row, col))
                booked_seats += 1

        else:
            print("Invalid Seat Number")


# Attendance Report
def attendance_report():

    for dept in range(1, 4):

        present_count = 0
        absent_count = 0

        for emp in range(1, 6):

            attendance = int(
                input(f"Department {dept} Employee {emp} Attendance (1/0): ")
            )

            if attendance == 1:
                present_count += 1

            elif attendance == 0:
                absent_count += 1

        print(
            f"Department {dept}: Present = {present_count}, Absent = {absent_count}"
        )


# Bank Transaction System
def bank_transactions():

    pin = 1234
    attempts = 0
    balance = 0

    total_transactions = 0
    total_withdraws = 0
    total_deposits = 0

    while attempts < 3:

        cpin = int(input("Enter PIN: "))

        if cpin == pin:

            print("\nMenu")
            print("Deposit")
            print("Withdraw")
            print("Balance")
            print("Mini Statement")
            print("Exit")

            while True:

                trans = input("Enter transaction type: ").lower()

                if trans == "deposit":

                    amount = int(input("Enter amount: "))
                    balance += amount
                    total_deposits += amount
                    total_transactions += 1

                    print("Deposit Successful")

                elif trans == "withdraw":

                    amount = int(input("Enter amount to withdraw: "))

                    if amount <= balance:

                        balance -= amount
                        total_withdraws += amount
                        total_transactions += 1

                        print("Withdrawal Successful")

                    else:

                        print("Insufficient Balance")

                elif trans == "balance":

                    print("Current Balance =", balance)

                elif trans == "mini statement":

                    print("\n----- Mini Statement -----")
                    print("Balance           :", balance)
                    print("Total Deposits    :", total_deposits)
                    print("Total Withdrawals :", total_withdraws)
                    print("Transactions      :", total_transactions)

                elif trans == "exit":

                    print("Thank You!")
                    break

                else:

                    print("Invalid Transaction")

            break

        else:

            print("Wrong PIN!")
            attempts += 1

    if attempts == 3:
        print("Your Card is Blocked")


# Uncomment the function you want to run

# student_grade_checker()
# atm_pin_verify()
# multiplication_table()
# number_guess()
# pattern()
# bus_seats()
# restaurant()
# cinema_booking()
# attendance_report()
bank_transactions()
