# sears.py

bill_thickness = 0.11 * 0.001
sears_height = 442
num_bills = 1
day = 1

while bill_thickness * num_bills < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', bill_thickness * num_bills)
