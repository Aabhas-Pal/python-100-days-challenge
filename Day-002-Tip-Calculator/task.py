#This the code for simple tip calculator and project of day 2 stay tuned for more interesting projects.
#Start this challenge with me lets code together!!
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

net_tip = (tip + 100)/100
total = ( (bill / 5) * net_tip )/people
print(f"According to given data each person should pay: ${total}")
print("Thank you for using our services")
