try:
	num1 = int(input("Enter First Number: "))
except ValueError:
	print("Please enter Number, try agin!")
	exit()
try:
	num2 = int(input("Enter Second Number: "))
except ValueError:
	print("Please enter Number, try agin!")
	exit()

choice = input("Enter the operation: (Operation +, -, *, /, %): ")

print(type(num1))
print(type(num2))
if choice == "+":
	sum = num1 + num2
	print("sum of tow numbers: ", sum)

elif choice == "-":
	sub = num1 - num2
	print("subsraction of tow numbers: ", sub)

elif choice == "*":
	multi = num1 * num2
	print("multifiction of tow numbers: ", multi)

elif choice == "/":
	div = num1 / num2
	print("Divesion of tow numbers: ", div)

elif choice == "%":
	rem = num1 % num2
	print("Remider of tow numbers: ", rem)
else:
	print("You entered invalid Choice, Try again")
