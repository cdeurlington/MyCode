#2.6 Sales Tax
print("2.6 SALES TAX")
purchase = float(input("Enter the amount of a purchase: $"))
state = 0.05*purchase
county = 0.025*purchase
total_tax = state + county
total_sale = purchase + total_tax
print("state sales tax: $" + str(state))
print("county sales tax: $" + str(county))
print("total sales tax: $" + str(total_tax))
print("total of sale: $" + str(total_sale))

#2.14 Compound Interest
print("2.14 COMPOUND INTEREST")
principal = float(input("principal amount deposited into the account: $"))
annual_interest = float(input("annual interest rate paid by the account: "))/100
compound = float(input("number of times per year interest is compounded: "))
term =  float(input("number of years the account earns interest: "))
amount = principal * ((1 + annual_interest/compound)**(term * compound))
print("Amount in account after specified number of years: $" + str(amount))

#3.10 Money Counting Game
print("3.10 MONEY COUNTING GAME")
print("Try to enter the number of coins required to make exactly one dollar.")
pennies = float(input("enter the number of pennies: ")) * 0.01
nickels = float(input("enter the number of nickels: ")) * 0.05
dimes = float(input("enter the number of dimes: ")) * 0.1
quarters = float(input("enter the number of quarters: ")) * 0.25
totalval = pennies + nickels + dimes + quarters
if(totalval == 1):
	print("Congratulations, you have won the game!")
elif(totalval > 1):
	print("You entered an amount greater than one dollar.")
elif(totalval < 1):
	print("You entered an amount less than one dollar.")

#3.12 Software Sales
print("3.12 SOFTWARE SALES")
quantity = float(input("How many packages were purchased? "))
if quantity >= 100:
	discount = 0.40
elif quantity >= 50:
	discount = 0.30
elif quantity >= 20:
	discount = 0.20
elif quantity >= 10:
	discount = 0.10
else:
	discount = 0
print("You received a discount of: " + str(discount * 100) + "%")
purchase_amount = 99 * quantity * (1 - discount)
print("Purchase Amount: $" + str(purchase_amount))

#3.13 Shipping Charges
print("3.13 SHIPPING CHARGES")
print("Enter the weight of your package in pounds.")
weight = float(input("Package weight: "))
if  weight <= 2:
	shipping_charges = 1.50
elif weight <= 6:
	shipping_charges = 3.00
elif weight <= 10:
	shipping_charges = 4.00
else:
	shipping_charges = 4.75
total_charges = shipping_charges * weight
print("Your shipping charges per pound are $" + str(shipping_charges))
print("Your total shipping charges are $" + str(total_charges))

#4.3 Budget Analysis
print("4.3 BUDGET ANALYSIS")
total_expense = 0
more = 'y'
budget = float(input("Enter how much you have budgeted for the month: $"))
print("Enter all your expenses for the month. ")
while more == 'y':
	expense = float(input("Enter an expense: $"))
	total_expense += expense
	more = input("Do you have any other expenses? (y for yes, n for no): ")
	total = budget - total_expense
def total(budget, total_expense):
	if budget > total_expense:
		total = budget - total_expense
		print("You are under your budget by $" + str(total))
	elif budget < total_expense:
		total = total_expense - budget
		print("You are over your budget by $" + str(total))
	else:
		print("You are exactly on your budget!")
total(budget, total_expense)

#4.5 Average Rainfall
print("4.5 AVERAGE RAINFALL")
year = 0
months = 12
rain = 0
years = int(input("Enter the period of years: "))
while year < years:
	month = 0
	for month in range(months):
		rainfall = float(input("Enter amount of rainfall this month (in inches): "))
		rain += rainfall
		month += 1
	year += 1
total_months = months * year
average = rain / total_months
print("Number of months measured: " + str(total_months))
print("Total rainfall for this period = " + str(rain) + " inches")
print("Average rainfall per month for this period = " + str(average) + " inches")

#4.12 Calculating the Factorial of a Number
print("4.12 CALCULATING THE FACTORIAL OF A NUMBER")
n = int(input("Enter a nonnegative integer you want to find the factorial of: "))
factorial = 1
for i in range(1, n+1, 1):
	factorial = factorial * i
print("The factorial of that number is " + str(factorial))

#8.4 Morse Code Converter
print("8.4 MORSE CODE CONVERTER")
morse_dict = {
	" ":" space ",
	",":"--..--",
	".":".-.-.-",
	"?":"..--..",
	"0":"-----",
	"1":".----",
	"2":"..---",
	"3":"...--",
	"4":"....-",
	"5":".....",
	"6":"-....",
	"7":"--...",
	"8":"---..",
	"9":"----.",
	"A":".-",
	"B":"-...",
	"C":"-.-.",
	"D":"-..",
	"E":".",
	"F":"..-.",
	"G":"--.",
	"H":"....",
	"I":"..",
	"J":".---",
	"K":"-.-",
	"L":".-..",
	"M":"--",
	"N":"-.",
	"O":"---",
	"P":".--.",
	"Q":"--.-",
	"R":".-.",
	"S":"...",
	"T":"-",
	"U":"..-",
	"V":"...-",
	"W":".--",
	"X":"-..-",
	"Y":"-.-",
	"Z":"--.."
	}
print("Enter a string.")
string = input("Insert your string here: ")
string = string.upper()
for i in string:
	print(morse_dict[i])