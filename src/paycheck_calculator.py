"""Calculate weekly pay using regular and overtime rates.

Input:
    Numeric hours worked during the week, entered by the user.

Process:
    Pay the first 40 hours at the regular rate and hours above 40 at
    the overtime rate.

Output:
    The employee's weekly paycheck, displayed on the screen.

Typical usage example:
    Enter 35 hours worked.
    The weekly paycheck is $700.0.
"""

# === Constants ===
REGULAR_RATE = 20
OVERTIME_RATE = 30
REGULAR_HOURS_LIMIT = 40


# === Main Function ===
def main() -> None:
    """Run the optional paycheck calculator practice program."""

    hours_worked = float(input("Enter the number of hours worked: "))

    if hours_worked > REGULAR_HOURS_LIMIT:
        regular_pay = REGULAR_HOURS_LIMIT * REGULAR_RATE
        overtime_hours = hours_worked - REGULAR_HOURS_LIMIT
        overtime_pay = overtime_hours * OVERTIME_RATE
        weekly_pay = regular_pay + overtime_pay
    else:
        weekly_pay = hours_worked * REGULAR_RATE

    print(f"The weekly paycheck is ${weekly_pay}")


# === Main Guard ===
if __name__ == "__main__":
    main()
