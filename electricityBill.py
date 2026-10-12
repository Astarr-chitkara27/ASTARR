# Electricity Bill Calculator
# Write a program that calculates the electricity bill based on units consumed using different rates for different slabs.

# 100 and below = 3
# 100-200 = 5
# 200-300 = 7
# 300 above = 10


# Taking Units Consumed as Input
#bug,fix= int(input("Enter Units Consumed: "));
units = int(input("Enter Units Consumed: "));

# Calculating Bill Based on Slabs
#bug= units==100, fix= units <= 100
if units <= 100:
    totalBill = units * 3;

#bug= units==200, fix=units <= 200
elif units <= 200:

#bug= totalBill = 100*3 + (units-100)*5, fix= totalBill = 100*3 + (units-100)*5;
    totalBill = 100*3 + (units-100)*5;

#bug= units==300, fix= units <= 300
elif units <= 300:
    totalBill = 100*3 + 100*5 + (units-200)*7;
#bug= totalBill = 100*3 + 100*5 + 100*7 + (units-300)*10, fix= totalBill = 100*3 + 100*5 + 100*7 + (units-300)*10;
else:
    totalBill = 100*3 + 100*5 + 100*7 + (units-300)*10;

# Displaying the Final Bill
print(f"Total Electricity Bill: {totalBill}");