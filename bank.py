salary = float(input("Please enter your monthly salary: ₱ "))

if(salary >= 30000):
       print("Congrats you are eligible for a loan!")
       loan = float(input("Enter the amount you want to apply for a loan: ₱ "))
       if(loan <= 10 * salary):
        payment = int(input("Choose how many months your payment term: "))
        interest = loan * 0.10
        total = loan + interest
        monthly_payment = total / payment

        print(f"Loan amount: ₱{loan:.2f}")
        print(f"10% interest: ₱{interest:.2f}")
        print(f"months to pay: {payment}")
        print(f"Your monthly payment is: ₱{monthly_payment:.2f}")
        print("Transaction complete!")

       else:
         print("you can't apply for a loan because the amount you requested exceeded 10 times your monthly salary")
else:       
        print("You are not eligible \nMonthly salary is too low to apply for a loan")