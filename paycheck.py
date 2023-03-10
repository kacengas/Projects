import time

#Base pay

def get_hourly_wage():
    return float(input("Enter your hourly wage: "))

def get_hours_worked():
    return float(input("How many hours did you work? "))

#Extra pay

def get_extra_hours_worked():
    evening_hours = 0
    inp = input("Do you work after 18? (y/n) ")
    if inp.lower() == "y" or inp.lower() == "yes":
        evening_hours = float(input("How many hours did you work after 18? "))
        extra_pay = float(input("How much extra are you paid each hour after 18? "))
        evening_hours *= extra_pay
    elif inp.lower() == "n" or inp.lower() == "no":
        pass
    else:
        print("Invalid input, please try again")
        return get_extra_hours_worked()
    return evening_hours

def get_sunday_pay():
    sunday_pay = 0
    inp = input("Do you work on Sundays? (y/n) ")
    if inp.lower() == "y" or inp.lower() == "yes":
        sunday_hours = float(input("How many hours did you work on Sundays? "))
        sunday_rate = float(input("How much extra are you paid for working on Sundays? "))
        sunday_pay = sunday_hours * sunday_rate
    elif inp.lower() == "n" or inp.lower() == "no":
        pass
    else:
        print("Invalid input, please try again")
        return get_sunday_pay()
    return sunday_pay

#Tax 

def get_tax_rate():
    percentage = 0
    while True:
        try:
            percentage = float(input("What is your tax rate as a percentage? "))
            break
        except ValueError:
            print("Invalid input, please enter a number")
    return percentage / 100.0

def get_fradrag():
    while True:
        try:
            return float(input("How much is your fradrag? "))
        except ValueError:
            print("Invalid input, please enter a number")

#Calculation

def print_calculating_message():
    print("Adding labor market contribution")
    print("Calculating paycheck...")

def calculate_paycheck(wage, hours, extra_hours, sunday_pay, tax_rate, fradrag):
    calculation = wage * hours
    extra_pay = extra_hours
    total_pay = calculation + extra_pay + sunday_pay
    labour = total_pay * 0.08
    tax_ready = total_pay - labour  
    akasse = tax_ready - fradrag
    tax = akasse * tax_rate 
    final = akasse - tax + fradrag
    print(f"Your paycheck for this month is {final:.2f} DKK")

while True:
    wage = get_hourly_wage()
    hours = get_hours_worked()
    extra_hours = get_extra_hours_worked()
    sunday_pay = get_sunday_pay()
    tax_rate = get_tax_rate()
    fradrag = get_fradrag()
    print_calculating_message()
    calculate_paycheck(wage, hours, extra_hours, sunday_pay, tax_rate, fradrag)
    time.sleep(2)
    repeat = input("Do you want to calculate another paycheck? (y/n) ")
    if repeat.lower() not in ['y', 'yes']:
        break