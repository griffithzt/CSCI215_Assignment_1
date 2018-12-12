#Zach Griffith
#Mortgage.py

#Purpose: The purpose of this program is to determine mortgage and interest rates of a loan.
#Input: Loan Amount, Months, Interest Rate.
#Output: Total Loan, Total Interest, Montly Payment Amount

#Certification of Authenticity:  
#I certify that this lab is entirely my own work.

def main():
    #Print user statement of purpose, and take loan amount input.
    print("Calculating your loan:")
    loan = eval(input("Enter Loan Amount: "))
    #Select the time from of the loan in months.
    months = eval(input("Enter Number of Months: "))
    #Select the interest rate percentage, print("Interest Rate")
    interest = eval(input("Enter the rate of interest: "))
    #Make interest input a decimal(example 5.3 into .053) for calculations
    rate = (interest / 100) /12
    #Output monthly loan amount
    a = loan *(rate*(1+rate)**months)
    b =((1+rate)**months -1)
    monthlyPayment = a/b
    print("Monthly Payment Amount: ", monthlyPayment)
    #Output lifetime loan total
    totalLoan = (months * monthlyPayment - loan) + loan
    print("Total Amount Paid: ", totalLoan)
    #Calculating total interest
    totalInterest = months * monthlyPayment - loan
    print("Lifetime Interest:", totalInterest)
#Running program
main()
